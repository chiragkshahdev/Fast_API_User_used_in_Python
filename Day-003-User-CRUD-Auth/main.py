from fastapi import FastAPI, Depends, HTTPException
from typing import List
from schemas import UserCreate, UserOut

app = FastAPI(title="Day 03 - FastAPI User API")

# Fake DB - Day 04 me isko SQLAlchemy se replace karenge
db = []

# --- DEPENDENCY - Ye hai Day 3 ka main topic ---
def check_duplicate_user(user: UserCreate):
    for u in db:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    if len(user.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be 6+ chars")
    return user

@app.get("/")
def home():
    return {"message": "Day 03 Working - User API Ready"}

@app.post("/users/", response_model=UserOut, tags=["Users"])
def create_user(user: UserCreate = Depends(check_duplicate_user)):
    new_user = {
        "id": len(db) + 1,
        "name": user.name,
        "email": user.email,
        "password": user.password # Real me hash hota hai, Day 05 me karenge
    }
    db.append(new_user)
    return new_user

@app.get("/users/", response_model=List[UserOut], tags=["Users"])
def get_users():
    return db

@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
def get_user_by_id(user_id: int):
    for user in db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")