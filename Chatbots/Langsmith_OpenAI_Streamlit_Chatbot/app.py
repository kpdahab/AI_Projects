import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

## Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")  # Set Langchain API key for tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"  # Enable Langchain tracing
os.environ['LANGCHAIN_PROJECT'] = "Q&A Chatbot with OpenAI"  # Set project name for tracking

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),  # System message for context
        ("user", "Question:{question}")  # User message template with a placeholder for the question
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    openai.api_type = api_key  # Set the OpenAI API key
    llm = ChatOpenAI(model=llm)  # Initialize the language model with the selected model
    output_parser = StrOutputParser()  # Initialize the output parser
    chain = prompt | llm | output_parser  # Create a processing chain with prompt, model, and parser
    answer = chain.invoke({'question': question})  # Invoke the chain with the user's question
    return answer  # Return the generated answer


## Title of the app
st.title("Q&A Chatbot With OpenAI")  # Set the title of the Streamlit app

## Sidebar for settings
st.sidebar.title("Settings")  # Title for the sidebar settings
api_key = st.sidebar.text_input("Enter your Open AI API Key:", type="password")  # Input for OpenAI API key

## Dropdown to select various Open AI Models
engine=st.sidebar.selectbox("Select an Open AI Model",["gpt-4o","gpt-4-turbo","gpt-4"]) # Model selection dropdown | # https://platform.openai.com/docs/models

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)  # Slider for temperature setting
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)  # Slider for max tokens setting

## Main interface for user input
st.write("Go ahead and ask any question")  # Prompt for user input
user_input = st.text_input("You:")  # Text input for user question

if user_input:
    response = generate_response(user_input, api_key, engine, temperature, max_tokens)  # Generate response
    st.write(response)  # Display the response
elif user_input:
    st.warning("Please enter the Open AI API Key in the sidebar")  # Warning if API key is missing
else:
    st.write("Please provide the user input")  # Prompt for user input if none is provided
