from fastapi import FastAPI, Query, Path
from typing import Optional

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@app.get("/users/")
async def read_users(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}, {"q": q}]}

    return results


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="Id of item", gt=1, le=10), q: Optional[str] = Query(None)
):
    results = {"item_id": item_id}

    if q:
        results.update({"q": q})
    return results
