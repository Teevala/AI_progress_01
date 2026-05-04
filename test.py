import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the client. It will automatically use the OPENAI_API_KEY from your .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Selitä AI-agentti yhdellä lauseella"}]
)

print(response.choices[0].message.content)