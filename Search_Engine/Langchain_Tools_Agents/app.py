import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize search tools for Arxiv, Wikipedia, and DuckDuckGo
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

search=DuckDuckGoSearchRun(name="search_engine")

# Set the title of the Streamlit app
st.title("Langchain SearchTrail: Intelligent Search and Recall")

# In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
#Try more Langchain Streamlit examples at (https://github.com/langchain-ai/streamlit-agent/).


# Sidebar for user settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

# Initialize session state for chat messages if not already set
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I am a chatbot who can search the web. How can I help you?"}
    ]

# Display chat messages from the session state
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input and generate responses
if prompt:= st.chat_input(placeholder="What is machine learning?"):
    # Append user input to session state messages
    st.session_state["messages"].append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    # Initialize the language model with the provided API key
    llm=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)

    # Combine search tools into a list
    tools=[wiki,arxiv,search]

    # Initialize the search agent with the tools and language model
    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

    # Generate and display the assistant's response
    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)

        # Extract the latest user input for the run method
        latest_user_input = st.session_state["messages"][-1]["content"]

        # Run the agent with the latest user input and display the response
        response = search_agent.run(input=latest_user_input, callbacks=[st_cb])
  
        st.session_state["messages"].append({'role':'assistant','content':response})
        st.write(response)

# Button to show conversation history
if st.button("Show Conversation History"):
    st.write("Conversation History:")
    for msg in st.session_state["messages"]:
        st.write(f"{msg['role'].capitalize()}: {msg['content']}")

# What are the key principles and applications of machine learning?