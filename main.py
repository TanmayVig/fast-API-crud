from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

db=[]

def bin_search(arr: list, low: int, high: int, x: int) -> int:
    mid = int((high - low)/2)
    if arr[mid].id == x:
        return mid
    else:
        if high > low:
            if arr[mid].id > x:
                return bin_search(arr,low, mid-1, x)
            elif arr[mid].id < x:
                return bin_search(arr, mid+1, high, x)
        else:
            return -1

class Todo(BaseModel):
    id: int 
    target_head: str
    target: str

    def __str__(self) -> str:
        return self.target_head


@app.get("/")
def index():
    return db



@app.post("/todo")
def set_task(task: Todo):
    task.id = db[-1].id + 1 if len(db) !=0 else 0
    db.append(task)
    return{"added":task}

@app.put("/todo")
def change_task(id: int, new_target_head: str, new_target: str):
    loc = bin_search(db,0, len(db)-1, id)
    if loc != -1:
        db[loc].target_head = new_target_head
        db[loc].target = new_target
        return db[loc]
    else:
        return {"message":"no such object"}


@app.delete("/todo")
def delete_task(id: int):
    loc = bin_search(db,0, len(db)-1, id)
    res = db.pop(loc)
    return res