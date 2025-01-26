# CodeWhisperer: AI-Powered Coding Assistant

## Project Overview

This project showcases an AI-powered coding assistant using **Gradio** and **CodeLlama**. The application is designed to assist developers by providing real-time coding suggestions and debugging support, enhancing productivity and interaction.

---

## Key Features

1. **Interactive User Interface**
   - Built with Gradio for a seamless user experience.
   - Allows users to input coding prompts and receive detailed suggestions.

2. **Real-Time Coding Assistance**
   - Utilizes CodeLlama for accurate syntax suggestions and debugging support.
   - Provides instant feedback to improve coding efficiency.

3. **Dynamic Interaction**
   - Maintains a session-based history for continuous interaction.

---

## Technologies Used

### Core Frameworks and Tools
- **Gradio**: Framework for building interactive web applications.
- **CodeLlama**: Model for providing coding assistance and suggestions.

### Backend Tools
- **Ollama**: For deploying and managing language models.

---

## How It Works

1. **User Input**: Users enter their coding prompts through a text input field.
2. **Processing**: The application uses CodeLlama to process the input and generate suggestions.
3. **Response Generation**: The model provides real-time coding recommendations and debugging support.
4. **Display Output**: The response is displayed in the Gradio interface.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/kpdahab/AI_Projects.git>
   cd <AI_Projects/Advanced_AI_Apps/CodeLlama_Coding_Assistant>

2.	**Install Dependencies**
   Ensure Python 3.12 is installed (conda create -p venv python==3.12), then activate venv and run:
   pip install -r requirements.txt

3.	**Set Up Ollama**: Run the following commands in the background:
   ollama run codellama
   cd C:\AI_Projects\Advanced_AI_Apps\CodeLlama_Coding_Assistant
   ollama create CodeWhisperer -f modelfile
   ollama run codewhisperer

4.	**Run the Application**
   Launch the Gradio application:
   python app.py

5.	**Interact with the Assistant**:
   Open the application in your web browser (http://localhost:7860/) and start asking questions.
   
---

### Disclaimer

This project is intended solely for demonstration purposes to showcase the use of Generative AI technologies. It is not meant for production use, and no contributions are accepted. If you have any questions or would like to discuss this project further, please reach out using the contact details below.

---

### License

This repository is for viewing purposes only and is not licensed for reuse or modification. All rights are reserved.