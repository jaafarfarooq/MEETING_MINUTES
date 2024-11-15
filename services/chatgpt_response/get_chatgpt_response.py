import openai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")
openai.api_key = os.getenv("openapi_apikey")

user_prompt="Act as a professional summary editor, \
Write a meeting minutes from the transcript. \
Add name of the participants \
Write in a simple way and detail key conclusions from the discussion. \
We have just finished our meeting here is our transcript."

def get_chatgpt_response(prompt):
    prompt = user_prompt + prompt
    try:
        # Send a request to the OpenAI API with the model, prompt, and max tokens
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify model name (e.g., "gpt-3.5-turbo" or "gpt-4")
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Optional system prompt
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Set token limit for response length
            temperature=0.7  # Adjust the creativity level (0.0 to 1.0)
        )

        # Extract and return the assistant's reply from the response
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
