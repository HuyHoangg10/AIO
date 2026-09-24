import streamlit as st
import random

# 1. TEXT ELEMENTS
st.title("Hello Hoang, đây là ứng dụng đầu tiên!")
st.header("1. Đây là Header")
st.subheader("2. Đây là Subheader")
st.text("Đây là văn bản định dạng thô (st.text)")
st.caption("Đây là chú thích nhỏ phía dưới (st.caption)")
st.write("Mọi thứ đã sẵn sàng để thực chiến với st.write.")

st.divider()

# 2. MARKDOWN & LATEX
st.markdown("# Đây là Tiêu đề cấp 1 (H1)")
st.markdown("## Đây là Tiêu đề cấp 2 (H2)")
st.markdown("### Đây là Tiêu đề cấp 3 (H3)")
st.markdown("Đây là chữ **in đậm** và đây là chữ *in nghiêng*.")
st.markdown("[Bấm vào đây để vào Google](https://google.com)")
st.markdown("""
- Thành phần thứ nhất
- Thành phần thứ hai
    - Thành phần con
""")
st.markdown("Hàm mất mát MSE được tính bằng công thức: $MSE = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2$")
st.markdown("<span style='color: red; font-weight: bold;'>Cảnh báo: Lỗi hệ thống!</span>", unsafe_allow_html=True)

st.divider()

# 3. CODE & ECHO
st.code("""
import random
value = random.randint(1, 10)
print(value)
""", language="python")

def get_year():
    return "2004"

with st.echo():
    st.write("This is a text")
    def get_name():
        return "Hoang"
    name = get_name()
    year = get_year()
    st.write(name, year)

st.divider()

# 4. BASIC WIDGETS
agree = st.checkbox("I agree")
if agree:
    st.write("Thanks")

status = st.radio(
    "Your fav team: ",
    ["Yellow", "Blue"],
    captions=["Vang", "Xanh"] # Thuộc tính để thêm chú thích nhỏ dưới từng lựa chọn
)

st.selectbox(
    "Your Contact",
    ["Email", "Address"]
)

st.multiselect(
    "Select color:",
    ["Yellow", "Red", "Blue"]
)

st.select_slider(
    "Select player:",
    ["Bruno", "Bryan", "Matheus"]
)

if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Gudbye")

st.text_input(
    "Your name",
    value="Hoang" # Thuộc tính đặt giá trị mặc định ban đầu
)

st.divider()

# 5. FILE UPLOADER (ĐÃ SỬA LỖI ĐỌC FILE)
upload_files = st.file_uploader(
    "Choose your file",
    accept_multiple_files=True # Thuộc tính cho phép chọn nhiều file cùng lúc (trả về 1 list)
)
for file in upload_files:
    read_f = file.read() # Sửa từ upload_file.read() thành file.read() để đọc đúng từng file trong vòng lặp
    st.write("File name:", file.name)

st.divider()

# 6. FORM & COLUMNS (ĐÃ SỬA HIỂN THỊ CỘT)
with st.form("my form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("Name: ")
    f_age = col2.text_input("Age: ") # Sửa từ col1 sang col2 để phân tách thành 2 cột rõ rệt

    submited = st.form_submit_button("Submit")
    if submited:
        st.write(f"Name: {f_name}, age: {f_age}")

st.divider()

# ==========================================
# 7. VÍ DỤ THỰC CHIẾN VỀ SESSION STATE (ỨNG DỤNG ĐẾM SỐ LẦN BẤM NÚT)
# ==========================================
st.subheader("Ví dụ minh họa Session State")

# Khởi tạo giá trị nếu chưa tồn tại trong bộ nhớ phiên
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

if "random_num" not in st.session_state:
    st.session_state["random_num"] = random.randint(1, 100)

# Tạo 2 cột để đặt nút bấm
col_btn1, col_btn2 = st.columns(2)

# Nút bấm 1: Tăng biến đếm (Trang web Rerun nhưng không làm mất giá trị counter cũ)
if col_btn1.button("Tăng số lần bấm"):
    st.session_state["counter"] += 1

# Nút bấm 2: Đổi số ngẫu nhiên mới hoàn toàn theo ý muốn
if col_btn2.button("Đổi số ngẫu nhiên mới"):
    st.session_state["random_num"] = random.randint(1, 100)

# Hiển thị kết quả sống sót qua các lần Rerun
st.write(f"🔢 Số lần bạn đã bấm nút: **{st.session_state['counter']}**")
st.write(f"🎯 Số ngẫu nhiên cố định (chỉ đổi khi bấm nút bên trên): **{st.session_state['random_num']}**")