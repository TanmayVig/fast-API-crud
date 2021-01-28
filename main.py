from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

db=[]

class Todo(BaseModel):
    id: int
    target_head: str
    target: str


@app.get("/")
def index():
    return db

# @app.get("/todo")
# def tasks():
#     return db

@app.post("/todo")
def set_task(task: Todo):
    db.append(task)
    return{"added":"true"}

@app.delete("/todo")
def delete_task(id: int):
    res = db.pop(id-1)
    return res