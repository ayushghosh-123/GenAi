from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyDznZds9dkv1jo4l9CYjPOeJa7fQIxnxZ0',
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {"role": "system", "content": "You are an expert in Math and only ans math question not other things"},
        {"role": "user", "content" : "Hey, whats your name ?"}
    ]
)

print(response.choices[0].message.content)