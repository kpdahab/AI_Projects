# Q&A Chatbot with OpenAI

## Project Overview

This project demonstrates the development of a Q&A chatbot using **Streamlit**, **OpenAI**, and **Langchain**. The chatbot is designed to provide intelligent responses to user queries by leveraging the capabilities of OpenAI's language models.

---

## Key Features

1. **Interactive User Interface**
   - Built with Streamlit for a user-friendly experience.
   - Allows users to input questions and receive answers in real-time.

2. **OpenAI Integration**
   - Utilizes OpenAI's language models to generate responses.
   - Supports various models for flexibility in response generation.

3. **Dynamic Prompting**
   - Uses a prompt template to structure user queries and responses.
   - Adapts to user input for personalized interactions.

4. **Configuration Options**
   - Users can set their OpenAI API key and select model parameters.
   - Adjustable settings for temperature and maximum tokens to control response creativity and length.

---

## Technologies Used

### Core Frameworks and Tools
- **Streamlit**: Framework for building interactive web applications.
- **OpenAI**: API for accessing powerful language models.
- **Langchain**: Framework for managing conversational AI workflows.

---

## How It Works

1. **User Input**: Users enter their questions through a text input field.
2. **Response Generation**: The application processes the input using the selected OpenAI model and generates a response.
3. **Display Output**: The generated response is displayed in the application interface.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/kpdahab/AI_Projects.git>
   cd <AI_Projects/Chatbots/Langsmith_OpenAI_Streamlit_Chatbot>

2.	Install Dependencies
   Ensure Python 3.10 is installed (conda create -p venv python==3.10), then run:
   pip install -r requirements.txt


3.	Set Up API Keys
   Add your API keys for the following services in a .env file:
   OPENAI_API_KEY=<your_openai_api_key>


4.	Run the Application
   Launch the Streamlit application:
   streamlit run app.py

5.	Interact with the chatbot:
   Open the application in your web browser (http://localhost:8501/) and start asking questions.

### Disclaimer

This project is intended solely for demonstration purposes to showcase the use of Generative AI technologies. It is not meant for production use, and no contributions are accepted. If you have any questions or would like to discuss this project further, please reach out using the contact details below.

### License

This repository is for viewing purposes only and is not licensed for reuse or modification. All rights are reserved.