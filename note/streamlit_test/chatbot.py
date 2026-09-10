# import streamlit as st
# from hugchat import hugchat
# from hugchat.login import Login

# # 1. Giao diện Sidebar nhập liệu
# with st.sidebar:
#     st.title("Chatbot")
#     hf_email = st.text_input("E-mail:")
#     hf_password = st.text_input("Password:", type="password")

# # 2. Khởi tạo lịch sử chat
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "How may i help you"}]

# # 3. Hiển thị lại toàn bộ lịch sử chat cũ (Dùng tên biến chạy msg để tránh trùng)
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# # 4. Hàm gọi API Hugchat
# def generate_response(prompt_input, email, passwd):
#     sign = Login(email, passwd)
#     cookies = sign.login()
#     chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
#     return chatbot.chat(prompt_input)

# # 5. Xử lý khi User nhập tin nhắn mới
# if prompt := st.chat_input(disabled=not (hf_email and hf_password)):
#     # Lưu và hiển thị ngay tin nhắn của User
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):  # SỬA LỖI: Chỉ định rõ giao diện "user"
#         st.write(prompt)

# # 6. Xử lý phản hồi của Bot (Chỉ chạy khi tin nhắn cuối cùng thuộc về User)
# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = generate_response(prompt, hf_email, hf_password)
#             st.write(response)
            
#     # Lưu tin nhắn của Bot vào lịch sử (Dùng tên biến mới để tránh trùng logic)
#     new_bot_message = {"role": "assistant", "content": str(response)}
#     st.session_state.messages.append(new_bot_message)


import streamlit as st
from hugchat import hugchat

# =====================================================================
# 🔥 BƯỚC QUAN TRỌNG: BẠN HÃY THAY COOKIES THỰC TẾ CỦA BẠN VÀO ĐÂY:
# (Mở hg/chat trên trình duyệt -> Ấn F12 -> tab Application -> Cookies)
# =====================================================================
HF_TOKEN = "RknTbVkxNJIqDBOnfGFyfpNMMHQKYUuAMwlsNnhJaLNbfLizJQCPXOrOWIVPbChDiDZKPDeFKjTkCnyewLNVmLpqpMbWpufzPwghKOEDdmrunvYTDhTeyslrYHAWbFvv"
HF_CHAT_COOKIE = "d131d98d-baae-4e88-9965-4ae03ef9bf95"


# 1. Giao diện Sidebar nhập liệu (Giữ lại để validate mở khóa ô chat)
with st.sidebar:
    st.title("Chatbot")
    hf_email = st.text_input("E-mail:")
    hf_password = st.text_input("Password:", type="password")

# 2. Khởi tạo lịch sử chat
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may i help you"}]

# 3. Hiển thị lại toàn bộ lịch sử chat cũ
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 4. Hàm gọi API Hugchat bằng Cookies ăn liền (Đã sửa đổi)
def generate_response(prompt_input):
    cookies_dict = {
        "token": HF_TOKEN,
        "hf-chat": HF_CHAT_COOKIE
    }
    # Khởi tạo thẳng ChatBot bằng cookie, không dùng hàm sign.login() lỗi thời nữa
    chatbot = hugchat.ChatBot(cookies=cookies_dict)
    return chatbot.chat(prompt_input)

# 5. Xử lý khi User nhập tin nhắn mới
if prompt := st.chat_input(disabled=not (hf_email and hf_password)):
    # Lưu và hiển thị ngay tin nhắn của User
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# 6. Xử lý phản hồi của Bot
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Gọi hàm mới (chỉ cần truyền câu prompt, không cần truyền email/mật khẩu)
            response = generate_response(prompt)
            st.write(response)
            
    # Lưu tin nhắn của Bot vào lịch sử
    new_bot_message = {"role": "assistant", "content": str(response)}
    st.session_state.messages.append(new_bot_message)