#Zero shot Prompting

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyDznZds9dkv1jo4l9CYjPOeJa7fQIxnxZ0',
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT='you should only and only ans the coding related question. Do not ans anything else. Your name is Alexa . If user asks something other than coodinhg, just say sorry'

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content" : "Hey, give your bio-data"}
    ]
)

print(response.choices[0].message.content)