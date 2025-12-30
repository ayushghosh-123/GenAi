from openai import OpenAI
import json


client = OpenAI(
    api_key='AIzaSyA925uPBaJdccxko2GDP9CjvHV4ZLHZ0wY',
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT='''
    you're an export AI Assistant in resolvong user queries using chain of throught. You work on START, PLAN and OUTPUT steps. You need to first PLAN what need to be done. The PLAN can be multiple steps . Once you think enough PLAN has been done, finally you can give an OUTPUT .

    Rules:
    - Strictly Follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (where user give an input), PLAN (That can be multiple times) and finally OUTPUT (WHICH IS GOING TO THE DISPLAYED TO THE USER)

    Output JSON Format:{
    "step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    START: Hey, can you solve 2+3*5/10
    PLAN: {
    "step": "PLAN": "content" : "Seems like user is interested problem"
    }
    PLAN: {
    "step": "PLAN": "content" : "looking at the problem, we should solve this using BODMAS method"
    }
    PLAN:{
    "step": "PLAN": "content" : "yes, The BODMAS is correct thing to be done "
    }
    PLAN:{
    "step": "PLAN": "content" : "first we must multiply 3*5 which is 15"
    }
    PLAN:{
    "step": "PLAN": "content" : "Now the new equation is 2 +15/10"
    }
    PLAN:{
    "step": "PLAN": "content" : "we must perform divided that is 15/10 = 1.5"
    }
    PLAN:{
    "step": "PLAN": "content" : "Now , the new equation is 2 + 1.5"
    }
    PLAN:{
    "step": "PLAN": "content" : "Now , finally lets perform add ans will be 3.5"
    }
    PLAN:{
    "step": "PLAN": "content" : "Great, we have solved and left with 3.5 ans"
    }
    OUTPUT:{
    "step": "OUTPUT": "content" : "3.5"
    }
'''
message_history=[
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input('please input ')
message_history.append({
    "role": "user",
    "content": user_query
})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages = message_history
    )
    
    raw_result = (response.choices[0].message.content)
    message_history.append({"role": "assistant", "content": raw_result})
    Parsed_result= json.loads(raw_result)

    if Parsed_result.get("step") == "START":
        print("fire",Parsed_result.get("content"))
        continue
    if Parsed_result.get('step') == "PLAN":
        print("water", Parsed_result.get("content"))
        continue
    if Parsed_result.get('step') == 'OUTPUT':
        print('cake', Parsed_result.get('content'))
        break