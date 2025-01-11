Here’s your README.md with Markdown formatting applied, exactly as per your draft:

# Generative AI Chatbot: Langchain, Groq API, Hugging Face, and ChromaDB

## Project Overview

This project demonstrates the development of an intelligent chatbot that integrates **Langchain**, **Groq API**, **Hugging Face**, and **ChromaDB** to deliver context-aware, efficient, and personalized interactions. By combining retrieval-based methods with generative AI, the chatbot provides accurate, human-like responses tailored to user queries.

---

## Key Features

1. **Message History Tracking**
   - Maintains session-based storage to enable a consistent flow of conversation.
   - Recalls past interactions for a seamless user experience.

2. **Prompt Templates**
   - Dynamic templates support multilingual responses.
   - Adapts responses based on context retrieved from relevant sources.

3. **Vector Store and Retrieval**
   - **Hugging Face Embeddings**: Converts text into vectors for similarity matching.
   - **ChromaDB**: Stores vectorized conversation data for efficient lookups.
   - **Retrievers**: Ensures contextually relevant outputs by pairing data with prompts.

4. **Chain Management**
   - Custom chains process user input, retrieve necessary information, and generate responses based on predefined workflows.

5. **Groq Integration**
   - Enhances model inference for fast response times and resource efficiency.

6. **Input Preprocessing with Trimmers**
   - Cleans and reduces input size using predefined criteria.
   - Improves response accuracy by removing irrelevant data.

---

## Technologies Used

### Core Frameworks and Tools
- **Langchain**: Framework for conversational AI.
- **Groq API**: High-performance engine for real-time inference.
- **Hugging Face**: Embeddings for natural language understanding.
- **ChromaDB**: Vector-based memory for interaction continuity.

### AI Techniques
- **Retrieval-Augmented Generation (RAG)**: Combines information retrieval with generative AI to provide accurate, fact-based answers.

---

## How It Works

1. **Input Preprocessing**: User inputs are cleaned and prepared using trimmers.
2. **Context Retrieval**: Relevant data is retrieved from ChromaDB using vector similarity.
3. **Dynamic Prompting**: The retrieved context is combined with predefined templates.
4. **Response Generation**: The system generates a personalized response using Hugging Face embeddings and Groq API.
5. **Session Continuity**: Message history is stored and utilized for ongoing conversations.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
    git clone <https://github.com/kpdahab/AI_Projects.git>
    cd <AI_Projects/Chatbots/Langchain_Groq_Chatbot>

2.	Install Dependencies
    Ensure Python 3.8+ is installed, then run:

    pip install -r requirements.txt


3.	Set Up API Keys
    Add your API keys for the following services in a .env file:

    GROQ_API_KEY=<your_groq_api_key>
    HUGGINGFACE_API_KEY=<your_huggingface_api_key>


4.	Run the Application
    Launch the Jupyter Notebook interface:

    Navigate to the Langchain_Groq_Chat folder.
	Open the .ipynb files and run the cells sequentially.


5.	Test the Chatbot
    Interact with the chatbot within the notebooks.
	Follow any additional instructions provided in the notebook cells to view and test the outputs.

Disclaimer

This project is intended solely for demonstration purposes to showcase the use of Generative AI technologies. It is not meant for production use, and no contributions are accepted. If you have any questions or would like to discuss this project further, please reach out using the contact details below.

License

This repository is for viewing purposes only and is not licensed for reuse or modification. All rights are reserved.

Contact

For questions or opportunities, feel free to reach out:
Email: [dahabkp@outlook.com]
LinkedIn: [https://www.linkedin.com/in/dahab-p-648968159]




