import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from the .env file
load_dotenv()

def generate_ai_response(prompt: str):
    # Initialize the Azure OpenAI Client
    # The client automatically picks up the API key and endpoint from environment variables,
    # but we explicitly pass them here for clarity.
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-10-21"  # Use the standard production API version
    )
    
    # Retrieve the model deployment name
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    
    try:
        # Create a chat completion request
        # Note: In Azure OpenAI, the 'model' parameter must match your DEPLOYMENT name
        completion = client.chat.completions.create(
            model=deployment_name, 
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful, concise AI assistant."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        # Extract and return the text response
        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = "Explain the difference between synchronous and asynchronous programming in two sentences."
    print(f"Sending prompt: '{user_prompt}'\n")
    
    response = generate_ai_response(user_prompt)
    print("--- AI Response ---")
    print(response)
