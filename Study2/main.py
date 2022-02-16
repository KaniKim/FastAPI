from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
import datetime

app = FastAPI()


class User(BaseModel):
    id: int
    message: Optional[str] = None
    creation_date: datetime.datetime
    is_valid: bool


@app.get("/")
async def main():
    return {"message": "Hello world!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}

    return {"item_id": item_id}


@app.post("/user/")
async def create_user(user: User, is_valid: bool = True):
    user_dict = user.dict()
    if user.message and is_valid:
        user_dict.update({"message": "Hello World User!"})

    return user_dict
