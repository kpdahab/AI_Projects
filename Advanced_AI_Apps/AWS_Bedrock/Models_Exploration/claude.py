import boto3
import json

prompt_data = "Act as an AI Engineer and write a funny poem" # Define the prompt for the AI model

bedrock = boto3.client(service_name="bedrock-runtime") # Initialize the Bedrock client using boto3

# Define the payload for the model. This includes the prompt and parameters for the text generation
payload={
    "prompt":prompt_data,
    "max_tokens_to_sample":512,
    "temperature":0.8,
    "top_p":0.8
}

body=json.dumps(payload) # Convert the payload to a JSON string
model_id="anthropic.claude-v2" # # Define the model ID. In this case, we're using Claude v2 from Anthropic.
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
response_text=response_body.get("completions")[0].get("data").get("text") 
print(response_text)