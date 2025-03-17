import streamlit as st

st.title("Contact Us 📞")
st.write("You can reach out to us via the form below.")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Submit"):
    st.success("Your message has been sent successfully!")
