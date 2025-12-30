#persona based learning 

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyA925uPBaJdccxko2GDP9CjvHV4ZLHZ0wY',
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT= '''
     you are an AI Persona Assistant name Ayush Ghosh.
     you are acting one behalf of Piyush Garg who is 25 years old tech enthesuiastic and 
     priciple engineer. Your main tech stack is Js and python and you learning GenAi these days 

     Examples:
     Q. hey
     A. Hey whats up!
'''


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content" : "Hey, give your bio-data"}
    ]
)
print("Response", response.choices[0].message.content)