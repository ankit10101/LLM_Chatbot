from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_gemini_response(query):
    response = model.generate_content(query)
    return response.text

st.set_page_config(
    initial_sidebar_state='expanded',
    layout="wide"
)

st.title("Gemini powered Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# def response_generator(prompt):
#     response = generate_gemini_response(prompt)
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = generate_gemini_response(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})