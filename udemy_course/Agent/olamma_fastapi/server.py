from typing import Union

from fastapi import FastAPI
from ollama import Client

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

