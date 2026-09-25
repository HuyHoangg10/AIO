import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

st.title("Chatbot")

with st.sidebar:
    st.title("Account")
    hf_email = st.text_input("Email:")
    hf_password = st.text_input("Password:", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I help you?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def generate_response(prompt_input, email, passwd):
    sign = Login(email, passwd)
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


is_ready = bool(hf_email and hf_password)
if prompt := st.chat_input(disabled=not is_ready):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"), st.spinner("Thinking..."):
        try:
            response = generate_response(prompt, hf_email, hf_password)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Đăng nhập thất bại hoặc gặp lỗi kết nối: {e}")
