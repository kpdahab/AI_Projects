import requests
import json
import gradio as gr


### Backend Code
url="http://localhost:11434/api/generate"  # https://github.com/ollama/ollama


headers = {
    'Content-Type': 'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model": "codewhisperer",
        "prompt": final_prompt,
        "stream": False # Only interested in the output, ignore the noise
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error",response.text)


### Front-End Code
interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text",
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
interface.launch()

