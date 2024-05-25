import streamlit as st
import os
import google.generativeai as genai

# Set up Google API key for generative AI
GOOGLE_API_KEY = "AIzaSyA9N2njOTvyKLi8_dF2lptU4uMWUEuB6dg"
api_key = os.getenv('GOOGLE_API_KEY', GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Run-GPT", page_icon="images/logo.png")

# Function to map model roles to Streamlit roles
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Initialize chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Add app logo at the top
st.image("images/logo.png", width=200)  # Adjust the width as needed


    st.title("Run-GPT!")

# Display additional information
st.subheader("Final Project in CCS 229 - Intelligent Systems")
st.subheader("Matthew Ariel A. Enarle - Section: BSCS 3-B AI")
st.write("This project utilizes Google Generative AI's Gemini model for conversation, offering an alternative to paid services like OpenAI's API.")

# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("Ask me any questions about Running!"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)

    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt)

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(response.text)
