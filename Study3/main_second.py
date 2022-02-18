from multiprocessing.spawn import import_main_path
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()


class Tags(BaseModel):
    tag_title: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tags: Optional[Tags] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="Id", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
    user: User
):
    results = {"item_id": item_id, "user": user}

    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
