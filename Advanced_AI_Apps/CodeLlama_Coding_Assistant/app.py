import requests
import json
import gradio as gr


### Backend Code
url="http://localhost:11434/api/generate"  # # API endpoint for generating responses | https://github.com/ollama/ollama


headers = {
    'Content-Type': 'application/json' # Set content type to JSON for the request
}

history=[]

def generate_response(prompt):
    history.append(prompt) # Add the new prompt to the history
    final_prompt="\n".join(history) # Combine all prompts into a single string

    data={
        "model": "codewhisperer", # Specify the model to use
        "prompt": final_prompt, # Send the combined prompt history
        "stream": False # Disable streaming, only get the final output
    }

    # Send a POST request to the API with the prompt data
    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text # Get the response text
        data=json.loads(response) # Parse the JSON response
        actual_response=data['response'] # Extract the actual response
        return actual_response # Return the response
    else:
        print("error",response.text) # Print error message if request fails


### Front-End Code
interface=gr.Interface(
    fn=generate_response, # Function to generate responses
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"), # Input textbox for user prompts
    outputs="text", # Output as text
    #css="style.css"  # Apply refined CSS for a cohesive grey and golden theme
    css="""
    body {
    background-color: #121212;
    color: #DAA520;  /* Golden color for text */
    font-family: 'Arial', sans-serif;
    }

    .gradio-container {
        background-color: #121212;
        color: #DAA520;  /* Golden color for text */
    }

    .gr-box {
        background-color: #333333 !important;  /* Grey color for background */
        color: #DAA520 !important;  /* Golden color for text */
        border: 2px solid #DAA520 !important;  /* Golden color for border */
        border-radius: 5px;
        padding: 10px;
    }

    input[type="text"], textarea {
        background-color: #333333 !important;  /* Grey color for background */
        color: #DAA520 !important;  /* Golden color for text */
        border: 2px solid #DAA520 !important;  /* Golden color for border */
        border-radius: 5px;
        padding: 10px;
    }

    button {
        background-color: #333333;  /* Grey color for background */
        color: #DAA520;  /* Golden color for text */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }

    button:hover {
        background-color: #444444;
    }
    """
)
interface.launch() # Launch the Gradio interface

