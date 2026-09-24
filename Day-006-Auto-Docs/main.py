from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

# Customizing Auto Docs
app = FastAPI(
    title="Day 6 - Auto Docs Mastery",
    description="""
    ## This is Day 6 of 100 Days of FastAPI 🚀

    This API demonstrates **How to make Professional Auto Documentation**.

    ### Features:
    * **Users** - Create and get users
    * **Products** - E-commerce style APIs
    * Auto validation with Pydantic

    ### Note:
    No need to write docs manually, FastAPI does it for you!
    """,
    version="2.0.0",
    contact={
        "name": "Chirag Shah",
        "url": "https://github.com/chiragkshahdev",
        "email": "chirag@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    docs_url="/docs", # Swagger UI
    redoc_url="/redoc", # ReDoc
    openapi_url="/openapi.json"
)

# --- Tags for grouping in docs ---
tags_metadata = [
    {"name": "Users", "description": "Operations with users. The **logic** for user management."},
    {"name": "Products", "description": "Manage products and inventory."},
]

# --- Pydantic Models with Examples (This is what makes docs beautiful) ---
class UserCreate(BaseModel):
    name: str = Field(..., example="Chirag Shah", description="Full name of user")
    email: str = Field(..., example="chirag@gmail.com", description="Valid email address")
    age: int = Field(..., gt=0, le=100, example=22, description="Age must be between 1-100")

    class Config:
        schema_extra = {
            "example": {
                "name": "Chirag Shah",
                "email": "chirag@gmail.com",
                "age": 22
            }
        }

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

class Product(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., example="MacBook Pro M3")
    price: float = Field(..., gt=0, example=1999.99)
    in_stock: bool = Field(default=True, example=True)

# --- Dummy DB ---
users_db = []
products_db = [
    {"id": 1, "title": "MacBook Pro M3", "price": 1999.99, "in_stock": True},
    {"id": 2, "title": "AirPods Pro", "price": 249.00, "in_stock": False}
]

# --- ROUTES WITH FULL DOCS ---

@app.get("/", tags=["Root"])
def root():
    """
    Welcome route - Shows that API is running.
    """
    return {"message": "Welcome to Day 6 - Auto Docs Demo", "docs": "/docs", "redoc": "/redoc"}

@app.post(
    "/users/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Create a new user",
    description="Create a new user with name, email and age. Email must be unique.",
    response_description="User created successfully"
)
def create_user(user: UserCreate):
    """
    - **name**: Full name
    - **email**: Must be valid and unique
    - **age**: Between 1-100
    """
    new_user = {"id": len(users_db) + 1, **user.dict()}
    users_db.append(new_user)
    return new_user

@app.get(
    "/users/",
    response_model=List[UserResponse],
    tags=["Users"],
    summary="Get all users"
)
def get_all_users():
    return users_db

@app.get(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Get user by ID",
    responses={
        404: {"description": "User not found"},
        200: {"description": "User found"}
    }
)
def get_user(user_id: int):
    if user_id > len(users_db) or user_id <= 0:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id - 1]

@app.get(
    "/products/",
    response_model=List[Product],
    tags=["Products"],
    summary="Get all products with stock filter"
)
def get_products(in_stock: bool = None, q: str = Field(None, description="Search query")):
    """
    Get products. You can filter by **in_stock** status.

    - **in_stock**: True/False
    - **q**: Search by title
    """
    result = products_db
    if in_stock is not None:
        result = [p for p in result if p["in_stock"] == in_stock]
    if q:
        result = [p for p in result if q.lower() in p["title"].lower()]
    return result