import streamlit as st

st.set_page_config(
    page_title="ทริปเที่ยวไทย | Streamlit",
    page_icon="✈️",
)

st.title("✈️ ยินดีต้อนรับสู่ประเทศไทย")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
if st.session_state.get("my_input"):
    st.write("You entered:", st.session_state["my_input"])