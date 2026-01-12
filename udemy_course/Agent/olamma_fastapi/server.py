from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()


def get_client():
    return Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contact-us")
def contact_us():
    return {"email": "ghoshayush910@gmail.com"}


@app.post("/chat")
def chat(message: str = Body(..., embed=True)):
    client = get_client()

    response = client.chat(
        model="gemma:2b",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return {
        "response": response.message.content  
    }
