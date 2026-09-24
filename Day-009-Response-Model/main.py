
### 💻 Code - `main.py`

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI(title="Day 09 - Response Model")

# DB Model (Internal)
class UserInDB(BaseModel):
    username: str
    email: str
    password: str
    full_name: str

# Response Model (Public - what client sees)
class UserPublic(BaseModel):
    username: str
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True

fake_db = {
    "chirag": {
        "username": "chirag",
        "email": "chirag@gmail.com",
        "password": "hashed_secret_123",
        "full_name": "Chirag Shah"
    }
}

@app.get("/")
def home():
    return {"message": "Day 09 - Response Model is working!"}

# CORE CONCEPT
@app.get("/users/{username}", response_model=UserPublic, tags=["Users"])
def get_user(username: str):
    """
    Returns user WITHOUT password because of response_model
    """
    return fake_db[username]

@app.get("/users", response_model=List[UserPublic], tags=["Users"])
def list_users():
    return list(fake_db.values())