import openai
from config import openrouter_api_key

# Set OpenRouter as base URL and key
openai.api_key = openrouter_api_key
openai.base_url = "https://openrouter.ai/api/v1"

def aiProcess(command):
    print(f"Sending to AI: {command}")
    try:
        client = openai.OpenAI(api_key=openrouter_api_key, base_url="https://openrouter.ai/api/v1")

        chat_completion = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant named Jarvis."},
                {"role": "user", "content": command}
            ]
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't reach the AI model. Please check your internet or API key."
