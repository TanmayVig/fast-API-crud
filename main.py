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



@app.post("/todo")
def set_task(task: Todo):
    db.append(task)
    return{"added":"true"}

@app.put("/todo")
def change_task(id: int, new_target_head: str, new_target: str):
    db[id-1].target_head = new_target_head
    db[id-1].target = new_target
    return db[id-1]


@app.delete("/todo")
def delete_task(id: int):
    res = db.pop(id-1)
    return res