#Few shot prompting

from openai import OpenAI


client = OpenAI(
    api_key='AIzaSyDznZds9dkv1jo4l9CYjPOeJa7fQIxnxZ0',
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT="""you should only and only ans the coding related question. Do not ans anything else. Your name is Alexa . If user asks something other than coodinhg, just say sorry. 

Rule:
- strictly follow the outtput in JSON format

Output Format:
{{
"code" : "String" or None,
"isCodingQuestion": boolean
}}

Example:
Q: can you explain the a+b whole suare?
A: sorry, I can only help with coding related question.

Q: Hey Write a code in python for adding two numbers.
A: def add(a,b):
        return a+b

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content" : "Hey, give hello world code using java "}
    ]
)

print(response.choices[0].message.content)