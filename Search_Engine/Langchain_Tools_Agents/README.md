# Langchain SearchTrail: Intelligent Search and Recall

## Project Overview

This project showcases an intelligent search and recall application using **Streamlit**, **Langchain**, and **Groq API**. The application is designed to assist users by searching the web and providing concise, relevant information from sources like Arxiv, Wikipedia, and DuckDuckGo.

---

## Key Features

1. **Interactive User Interface**
   - Built with Streamlit for a seamless user experience.
   - Allows users to input queries and receive detailed responses.

2. **Multi-Source Search Integration**
   - Utilizes Arxiv, Wikipedia, and DuckDuckGo for comprehensive search capabilities.
   - Provides concise and relevant information from multiple sources.

3. **Dynamic Chat Interface**
   - Maintains a session-based chat history for continuous interaction.
   - Displays both user queries and assistant responses in a chat format.

4. **Customizable Settings**
   - Users can input their Groq API key for personalized interactions.
   - Adjustable settings for search and response parameters.

---

## Technologies Used

### Core Frameworks and Tools
- **Streamlit**: Framework for building interactive web applications.
- **Langchain**: Framework for managing conversational AI workflows.
- **Groq API**: API for accessing advanced language models.

### Search Tools
- **ArxivAPIWrapper**: For retrieving academic papers.
- **WikipediaAPIWrapper**: For accessing Wikipedia articles.
- **DuckDuckGoSearchRun**: For general web searches.

---

## How It Works

1. **User Input**: Users enter their queries through a chat input field.
2. **Search and Retrieval**: The application uses integrated search tools to gather information.
3. **Response Generation**: The language model processes the input and generates a response.
4. **Display Output**: The response is displayed in the chat interface.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/kpdahab/AI_Projects.git>
   cd <AI_Projects/Search_Engine/Langchain_Tools_Agents>

2.	**Install Dependencies**
   Ensure Python 3.10 is installed (conda create -p venv python==3.10), then activate venv and run:
   pip install -r requirements.txt


3.	**Set Up API Keys**
   Add your API keys for the following services in a .env file:
   GROQ_API_KEY=<your_groq_api_key>


4.	**Run the Application**
   Launch the Streamlit application:
   streamlit run app.py

5.	**Interact with the chatbot**:
   Open the application in your web browser (http://localhost:8501/) and start asking questions.
   
---

### Disclaimer

This project is intended solely for demonstration purposes to showcase the use of Generative AI technologies. It is not meant for production use, and no contributions are accepted. If you have any questions or would like to discuss this project further, please reach out using the contact details below.

---

### License

This repository is for viewing purposes only and is not licensed for reuse or modification. All rights are reserved.