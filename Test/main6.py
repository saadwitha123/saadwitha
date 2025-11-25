#Complete CRUD Operations (in-memory list)
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []

class Item(BaseModel):
    id: int
    name: str

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: Item):
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = new_item
            return new_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
