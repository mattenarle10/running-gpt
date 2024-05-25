## 🏃 Run-GPT: A Streamlit App for Interactive Conversation with Gemini by Matt E.

**Run GPT** is a web app built with Streamlit that allows you to have interactive conversations about running using Google Generative AI's powerful Gemini model.  This project provides a user-friendly interface for exploring the capabilities of large language models for free, offering an alternative to paid services!  

**Features:**

* **Conversational Interface:** Interact with Gemini through a chat-like interface, asking questions and receiving informative responses.
* **Streamlit Integration:** Built with Streamlit for a smooth and responsive user experience. ⚡
* **Gemini Model Power:** Leverages the capabilities of Google Generative AI's Gemini model for high-quality text generation.

**Getting Started / How to if u want to try!:**

1. Clone this repository.
2. Install required dependencies: `pip install streamlit google-generativeai` (ensure you have a Google Cloud project with the Generative AI API enabled).
3. Set your Google API key as an environment variable named `GOOGLE_API_KEY`. (You can find your API key in the Google Cloud Console)
4. Run the app: `streamlit run app.py`

**Code Structure:**

The code is well-structured, utilizing Streamlit components for a user-friendly interface. Key elements include:

* **API Key Configuration:** Securely stores the Google API key using environment variables. 
* **Chat History Management:** Maintains chat history in the session state for context-aware conversation.
* **Chat Display:** Displays previous messages and user input in a chat-like format.
* **User Input:** Accepts user prompts through a chat input box.
* **Gemini Interaction:** Sends user prompts to the Gemini model and displays the generated response.

**Customization:**

* Feel free to modify the app's title, logo, and descriptions to personalize your experience.
* Try to explore streamlit

**Project by:**

* Matthew Ariel A. Enarle - Section: BSCS 3-B AI
* All thanks and credits goes to Prof. Louie Cervantes for teaching us! Thank you Sir

**This project serves as a final project for CCS 229 - Intelligent Systems.**
