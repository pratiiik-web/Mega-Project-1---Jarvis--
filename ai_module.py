# ai_module.py

import openai
from config import openrouter_api_key

# Configure OpenRouter
openai.api_key = openrouter_api_key
openai.api_base = "https://openrouter.ai/api/v1"

def aiProcess(command):
    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # free model
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud. Keep responses short."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Sorry, I couldn't reach the AI model. Please check your internet or API key."
