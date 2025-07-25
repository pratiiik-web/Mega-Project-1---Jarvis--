import openai

# Set OpenRouter API key and base URL
openai.api_key = "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"  # replace this with your actual OpenRouter API key
openai.api_base = "https://openrouter.ai/api/v1"

# Send chat request
response = openai.ChatCompletion.create(
    model="mistralai/mistral-7b-instruct",  # free model on OpenRouter
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message.content)
