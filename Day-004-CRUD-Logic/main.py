from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Day 4 - CRUD Logic API", version="1.0.0")

# 1. Pydantic Model - Data ka Shape
class Item(BaseModel):
    id: int
    name: str
    price: float
    is_avenger_gear: bool = False

# 2. Fake Database - In-Memory
fake_db: List[Item] = []

# 3. CREATE - POST
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    for existing_item in fake_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    fake_db.append(item)
    return item

# 4. READ ALL - GET
@app.get("/items/", response_model=List[Item])
def get_all_items():
    return fake_db

# 5. READ ONE - GET by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# 6. UPDATE - PUT
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(fake_db):
        if item.id == item_id:
            fake_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found for update")

# 7. DELETE - DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(fake_db):
        if item.id == item_id:
            del fake_db[index]
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found for delete")

# 8. Home Route
@app.get("/")
def home():
    return {"message": "Day 4 CRUD API is Online - CAIO Protocol"}