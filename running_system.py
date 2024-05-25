import streamlit as st
import os
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyA9N2njOTvyKLi8_dF2lptU4uMWUEuB6dg"
api_key = os.getenv('GOOGLE_API_KEY', GOOGLE_API_KEY)

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.level = 0

st.title("Final Project in CCS 229 - Intelligent Systems")
st.subheader("Matthew Ariel A. Enarle - Section: BSCS 3-B AI")
st.write("This project utilizes Google Generative AI's Gemini model for conversation, offering an alternative to paid services like OpenAI's API.")

# Define the multi-level prompts
prompts = [
    "What is your current running experience (e.g., beginner, intermediate, advanced)?",
    "What are your running goals (e.g., distance, speed, health)?",
    "I can help you create a personalized running plan. Ask me Questions!"
]

# Create a scrollable container for chat messages
chat_container = st.container()

# Display chat messages from history above current input box
with chat_container:
    st.write('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)
    st.write('</div>', unsafe_allow_html=True)

# Accept user's next message, add to context, resubmit context to Gemini
if st.session_state.level < len(prompts):
    current_prompt = prompts[st.session_state.level]
    if prompt := st.chat_input(current_prompt):
        # Display user's last message
        st.chat_message("user").markdown(prompt)

        # Send user entry to Gemini and read the response
        response = st.session_state.chat.send_message(prompt)

        # Add the new message to the chat history
        st.session_state.chat.history.append(response)

        # Display the last response
        with st.chat_message("assistant"):
            st.markdown(response.text)

        # Move to the next level
        st.session_state.level += 1
else:
    if prompt := st.chat_input(prompts[-1]):
        # Display user's last message
        st.chat_message("user").markdown(prompt)

        # Send user entry to Gemini and read the response
        response = st.session_state.chat.send_message(prompt)

        # Add the new message to the chat history
        st.session_state.chat.history.append(response)

        # Display the last response
        with st.chat_message("assistant"):
            st.markdown(response.text)
