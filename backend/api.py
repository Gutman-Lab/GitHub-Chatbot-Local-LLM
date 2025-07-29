from fastapi import FastAPI
from pydantic import BaseModel
from backend.chat.rag_chat import chat_with_repo

app = FastAPI()

class Query(BaseModel):
    question: str
    model: str = "mistral:latest"

@app.post("/chat")
def ask_question(query: Query):
    response = chat_with_repo(query.question, model=query.model)
    return {"response": response}
