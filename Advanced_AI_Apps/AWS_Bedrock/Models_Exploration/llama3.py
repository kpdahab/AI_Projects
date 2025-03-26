import boto3
import json

# Define the prompt for the AI model
prompt_data = """
Act as an AI Engineer and write a funny poem
"""

# Initialize the Bedrock client using boto3
bedrock = boto3.client(service_name="bedrock-runtime")

# Define the payload for the model. This includes the prompt and parameters for the text generation.
payload={
    "prompt":"[INST]"+ prompt_data +"[INST]",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

# Convert the payload to a JSON string
body=json.dumps(payload) 

model_id="meta.llama3-70b-instruct-v1:0" # Define the model id - #Llama 3 70B Instruct

# Invoke the model with the payload and get the response
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Parse the response body from the model
response_body=json.loads(response.get("body").read())

# Extract the generated text from the response
response_text=response_body['generation']
print(response_text)