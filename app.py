import streamlit as st

st.title("My AI App 🚀")
st.write("Welcome to my Streamlit website")

# 1. Create a text box for the user to type in
user_prompt = st.text_input("What would you like to ask the AI?")

# 2. Check if the button is clicked
if st.button("Send"):
    # 3. Check if the user actually typed something
    if user_prompt: 
        st.success(f"You asked: {user_prompt}")
        st.info("The AI's actual response will go here soon!")
    else:
        st.warning("Please type a message first.")
