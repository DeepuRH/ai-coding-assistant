import streamlit as st

st.title("My AI App 🚀")
st.write("Welcome to my Streamlit website")
st.write("this is my first App creation project!")

# Connect the button to an action using an 'if' statement
if st.button("click"):
    # Everything indented under here happens ONLY when the button is clicked
    st.success("You clicked the button! It works!")
    st.balloons() # This adds a fun animation!
