import uvicorn
from fastapi import FastAPI

from app.model import PostSchema

posts = [{}]
users = []

app = FastAPI()


@app.get("/", tags=["test"])
def greet(): 
    return {"Hello": "World"}

 