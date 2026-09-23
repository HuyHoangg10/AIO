import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import chainlit as cl


# Helper function to format retrieved documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


@cl.on_chat_start
async def on_chat_start():
    # 1. Notify user that initialization is in progress
    msg = cl.Message(content="Loading documents and building RAG pipeline...")
    await msg.send()

    # 2. Document Loading & Splitting
    file_path = "./YOLOv10_Tutorials.pdf"
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    # 3. Vector Embedding & Database
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_db = Chroma.from_documents(documents=chunks, embedding=embedding_model)
    retriever = vector_db.as_retriever()

    # 4. LLM Configuration
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=2)

    # 5. Prompt Definition
    prompt_template = """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you do not know the answer, just say that you do not know. Keep the answer concise.

Context:
{context}

Question:
{question}

Answer:"""

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # 6. Assemble RAG Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # 7. Store the chain in user session
    cl.user_session.set("rag_chain", rag_chain)

    # Update notification message
    msg.content = "System is ready! Ask me anything about YOLOv10."
    await msg.update()


@cl.on_message
async def on_message(message: cl.Message):
    # Retrieve the initialized chain from session
    rag_chain = cl.user_session.get("rag_chain")

    # Invoke chain with user question
    response = await rag_chain.ainvoke(message.content)

    # Send response back to the UI
    await cl.Message(content=response).send()
