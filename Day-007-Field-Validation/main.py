from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator, EmailStr, HttpUrl
from typing import List, Optional
from datetime import date
import re

app = FastAPI(
    title="Day 7 - Field Validation",
    description="Master Pydantic Field Validation in FastAPI",
    version="1.0
"
)

# --- 1. BASIC FIELD VALIDATIONS ---

class UserBasic(BaseModel):
    # String validations
    username: str = Field(
       ...,
        min_length=3,
        max_length=20,
        regex="^[a-zA-Z0-9_]+$",
        description="Only alphanumeric and underscore, 3-20 chars",
        example="chirag_123"
    )

    # Number validations
    age: int = Field(..., gt=0, lt=120, description="Age 1-119", example=22)
    price: float = Field(..., gt=0, description="Must be positive", example=99.99)

    # List validation
    tags: List[str] = Field(..., min_items=1, max_items=5, example=["python", "fastapi"])

# --- 2. ADVANCED VALIDATION MODEL (For Registration) ---

class UserRegister(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, example="Chirag Shah")
    email: EmailStr = Field(..., example="chirag@gmail.com", description="Auto validates email format")
    password: str = Field(..., min_length=8, description="Min 8 chars")
    confirm_password: str = Field(..., example="MyPass123@")
    age: int = Field(..., ge=18, le=100, example=22, description="Must be 18+")
    website: Optional[HttpUrl] = Field(None, example="https://chirag.dev")
    dob: date = Field(..., description="Date of Birth")
    phone: str = Field(..., example="+91-9876543210")

    # --- Custom Validator 1: Password Match ---
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v!= values['password']:
            raise ValueError('Passwords do not match')
        return v

    # --- Custom Validator 2: Password Strength ---
    @validator('password')
    def password_strong(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r"[0-9]", v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r"[@$!%*?&]", v):
            raise ValueError('Password must contain at least one special character (@$!%*?&)')
        return v

    # --- Custom Validator 3: Phone Format ---
    @validator('phone')
    def phone_valid(cls, v):
        pattern = r"^\+?[0-9\s-]{10,15}$"
        if not re.match(pattern, v):
            raise ValueError('Invalid phone number format')
        return v

    # --- Custom Validator 4: Age vs DOB ---
    @validator('dob')
    def dob_not_future(cls, v):
        if v > date.today():
            raise ValueError('DOB cannot be in future')
        return v

    class Config:
        schema_extra = {
            "example": {
                "name": "Chirag Shah",
                "email": "chirag@gmail.com",
                "password": "StrongPass123@",
                "confirm_password": "StrongPass123@",
                "age": 22,
                "website": "https://chirag.dev",
                "dob": "2002-01-15",
                "phone": "+91-9876543210"
            }
        }

# --- 3. Product with More Field Types ---

class Product(BaseModel):
    name: str = Field(..., min_length=3, example="MacBook Pro")
    price: float = Field(..., gt=0, le=100000, example=1999.99)
    discount: Optional[int] = Field(0, ge=0, le=90, description="0-90% discount")
    sku: str = Field(..., regex="^[A-Z]{3}-[0-9]{4}$", example="APP-1234", description="Format: XXX-1234")
    quantity: int = Field(..., ge=0, description="Stock quantity")

# --- APIs ---

@app.get("/")
def home():
    return {"message": "Day 7 - Field Validation Working!", "docs": "/docs"}

@app.post("/validate-basic/", tags=["Basic Validation"])
def validate_basic(user: UserBasic):
    return {"message": "Basic validation passed!", "data": user}

@app.post("/register/", tags=["Advanced Validation"], status_code=201)
def register_user(user: UserRegister):
    """
    Try these invalid cases in /docs to see validation errors:
    - Weak password: `chirag123`
    - Mismatched passwords
    - Age < 18
    - Future DOB
    - Invalid phone
    """
    return {
        "message": f"User {user.name} registered successfully!",
        "email": user.email,
        "note": "All validations passed"
    }

@app.post("/products/", tags=["Product Validation"])
def create_product(product: Product):
    final_price = product.price * (1 - product.discount/100)
    return {
        "message": "Product created",
        "product": product,
        "final_price_after_discount": round(final_price, 2)
    }

# --- Custom error message example ---
@app.get("/items/{item_id}", tags=["Path Validation"])
def get_item(item_id: int = Field(..., gt=0, lt=1000, description="ID must be 1-999")):
    if item_id == 13:
        raise HTTPException(status_code=400, detail="Item 13 is unlucky, not available!")
    return {"item_id": item_id}