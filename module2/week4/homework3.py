import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vi_data_df = pd.read_csv("./vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()

context_embedded = tfidf_vectorizer.fit_transform(context)

val_10 = context_embedded.toarray()[7][0]
print(f"Câu 10: {round(val_10, 2)}")  


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # Lowercasing và dùng transform để mã hóa câu truy vấn
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    
    # Tính cosine similarity giữa query và toàn bộ context
    cosine_scores = cosine_similarity(query_embedded, context_embedded).flatten()
    
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
        
    return results

question = vi_data_df.iloc[0]['question']
results_11 = tfidf_search(question, tfidf_vectorizer, top_d=5)
val_11 = results_11[0]['cosine_score']
print(f"Câu 11: {round(val_11, 2)}")

def corr_search(question, tfidf_vectorizer, top_d=5):
    # Lowercasing và dùng transform để mã hóa câu truy vấn
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    
    # Chuyển sang mảng thường và tính Pearson correlation bằng np.corrcoef
    corr_scores = np.corrcoef(query_embedded.toarray(), context_embedded.toarray())
    corr_scores = corr_scores[0][1:]
    
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
        
    return results

results_12 = corr_search(question, tfidf_vectorizer, top_d=5)
val_12 = results_12[1]['corr_score']
print(f"Câu 12: {round(val_12, 2)}")  