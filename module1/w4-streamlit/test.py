import streamlit as st

st.title("HELLO IT's MY PROJECT")

st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")


st.code("""
    name = "Hoang"
    print(f"Toi ten la f{name}")
""")

with st.echo():
    def get_name():
        return "HH"
    name = get_name()    
    st.write(name)

st.divider()


agree = st.checkbox("I agree")

st.radio(
    "Your fav player of MU",
    ["Bruno","M5","Cunha"],
    captions=["captain","cb","st"]
)

st.selectbox("Your contact",["Email","Phone number"])

st.multiselect("Colors",("Yellow","Blue","Green"))

st.select_slider("Colors",range(50))

if st.button("say hell"):
    st.write("hello")
else:
    st.write("bye")

st.text_input("Your name",value="Hoang ngo vin")


st.divider()

with st.form("my form"):
    col_1 , col_2 = st.columns(2)
    name = col_1.text_input("Name")
    age = col_2.text_input("Age")

    submited = st.form_submit_button("Submit please")
    if submited:
        st.write(f"Name: {name}, Age: {age}")