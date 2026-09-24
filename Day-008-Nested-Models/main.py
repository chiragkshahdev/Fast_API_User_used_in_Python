from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Day 8 - Nested Models",
    description="Learn Nested Models like E-commerce, Blog, User with Address",
    version="1.0
"
)

# --- NESTED MODEL 1: Address inside User ---

class Address(BaseModel):
    street: str = Field(..., example="123 MG Road")
    city: str = Field(..., example="Mumbai")
    state: str = Field(..., example="Maharashtra")
    pincode: str = Field(..., min_length=6, max_length=6, regex="^[0-9]{6}$", example="400001")
    country: str = Field(default="India", example="India")

class User(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Chirag Shah")
    email: EmailStr = Field(..., example="chirag@gmail.com")
    address: Address # <-- NESTED MODEL
    shipping_address: Optional[Address] = None # Optional nested

# --- NESTED MODEL 2: E-commerce Product with Multiple Nested ---

class Brand(BaseModel):
    name: str = Field(..., example="Apple")
    website: str = Field(..., example="https://apple.com")

class Category(BaseModel):
    id: int = Field(..., example=101)
    name: str = Field(..., example="Laptops")
    slug: str = Field(..., example="laptops")

class Review(BaseModel):
    user_id: int = Field(..., example=1)
    username: str = Field(..., example="Aman")
    rating: int = Field(..., ge=1, le=5, example=5)
    comment: str = Field(..., example="Amazing product!")
    created_at: datetime = Field(default_factory=datetime.now)

class Product(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., example="MacBook Pro M3 Max")
    price: float = Field(..., gt=0, example=2499.99)
    brand: Brand # Nested 1
    category: Category # Nested 2
    tags: List[str] = Field(default=[], example=["apple", "m3", "laptop"])
    reviews: List[Review] = [] # List of Nested Models
    specifications: dict = Field(default={}, example={"RAM": "32GB", "SSD": "1TB"})

    @property
    def average_rating(self):
        if not self.reviews:
            return 0
        return round(sum(r.rating for r in self.reviews) / len(self.reviews), 1)

# --- NESTED MODEL 3: Blog Post ---

class Author(BaseModel):
    id: int
    name: str
    avatar: str = Field(..., example="https://i.pravatar.cc/150?img=32")

class Comment(BaseModel):
    id: int
    author: Author # Nested inside nested
    text: str
    likes: int = 0

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    author: Author
    comments: List[Comment] = []
    related_posts: Optional[List['BlogPost']] = None # Self-referencing nested

BlogPost.update_forward_refs()

# --- DUMMY DATA ---

sample_product = {
    "id": 1,
    "title": "MacBook Pro M3 Max",
    "price": 2499.99,
    "brand": {"name": "Apple", "website": "https://apple.com"},
    "category": {"id": 101, "name": "Laptops", "slug": "laptops"},
    "tags": ["apple", "m3", "laptop", "pro"],
    "reviews": [
        {"user_id": 1, "username": "Chirag", "rating": 5, "comment": "Best laptop ever!"},
        {"user_id": 2, "username": "Aman", "rating": 4, "comment": "Great performance but costly"}
    ],
    "specifications": {"RAM": "36GB", "Storage": "1TB SSD", "Chip": "M3 Max"}
}

# --- APIs ---

@app.get("/")
def home():
    return {"message": "Day 8 - Nested Models Working!", "docs": "/docs"}

@app.post("/users/", response_model=User, tags=["Users"])
def create_user(user: User):
    """Create user with nested address object"""
    return user

@app.get("/users/example", response_model=User, tags=["Users"])
def get_example_user():
    return {
        "id": 1,
        "name": "Chirag Shah",
        "email": "chirag@gmail.com",
        "address": {
            "street": "123 MG Road, Virar West",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "401303",
            "country": "India"
        },
        "shipping_address": {
            "street": "456 Office Complex",
            "city": "Pune",
            "state": "Maharashtra",
            "pincode": "411001",
            "country": "India"
        }
    }

@app.get("/products/example", response_model=Product, tags=["Products"])
def get_example_product():
    return sample_product

@app.post("/products/", response_model=Product, tags=["Products"])
def create_product(product: Product):
    """Create product with brand, category, and list of reviews - Full nested"""
    return product

@app.post("/blog/", tags=["Blog"])
def create_blog_post(post: BlogPost):
    return {
        "message": "Blog created",
        "title": post.title,
        "author": post.author.name,
        "total_comments": len(post.comments),
        "avg_comment_likes": sum(c.likes for c in post.comments) / len(post.comments) if post.comments else 0
    }

@app.get("/blog/example", tags=["Blog"])
def get_example_blog():
    return {
        "id": 1,
        "title": "Understanding Nested Models in FastAPI",
        "content": "Nested models are very important...",
        "author": {"id": 1, "name": "Chirag Shah", "avatar": "https://i.pravatar.cc/150?img=32"},
        "comments": [
            {
                "id": 1,
                "author": {"id": 2, "name": "Aman", "avatar": "https://i.pravatar.cc/150?img=2"},
                "text": "Great explanation!",
                "likes": 10
            },
            {
                "id": 2,
                "author": {"id": 3, "name": "Priya", "avatar": "https://i.pravatar.cc/150?img=5"},
                "text": "Very helpful, thanks!",
                "likes": 5
            }
        ]
    }