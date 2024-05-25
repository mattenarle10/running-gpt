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

# Set custom CSS to make the header fixed and the chat container scrollable
st.markdown(
    """
    <style>
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: white;
        z-index: 1000;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .scrollable-chat {
        margin-top: 150px; /* Adjust based on header height */
        height: calc(100vh - 200px); /* Adjust based on header/footer height */
        overflow-y: auto;
        padding-right: 15px; /* Prevents hiding content behind scrollbar */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Fixed header
st.markdown('<div class="fixed-header">', unsafe_allow_html=True)
st.title("Final Project in CCS 229 - Intelligent Systems")
st.subheader("Matthew Ariel A. Enarle - Section: BSCS 3-B AI")
st.write("This project utilizes Google Generative AI's Gemini model for conversation, offering an alternative to paid services like OpenAI's API.")
st.markdown('</div>', unsafe_allow_html=True)

# Create a scrollable container for chat messages
st.markdown('<div class="scrollable-chat">', unsafe_allow_html=True)
with st.container():
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Accept user's next message, add to context, resubmit context to Gemini
    if prompt := st.chat_input("I can help you create a personalized running plan. Ask me Questions!"):
        # Display user's last message
        st.chat_message("user").markdown(prompt)

        # Send user entry to Gemini and read the response
        response = st.session_state.chat.send_message(prompt)

        # Add the new message to the chat history
        st.session_state.chat.history.append(response)

        # Display the last response
        with st.chat_message("assistant"):
            st.markdown(response.text)
st.markdown('</div>', unsafe_allow_html=True)
