from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Day 5 - HTTP Exception Demo",
    description="Learn all types of HTTP Exceptions in FastAPI",
    version="1.0"
)

# Dummy Database
fake_db = {
    1: {"id": 1, "name": "Chirag", "role": "Developer"},
    2: {"id": 2, "name": "Aman", "role": "Designer"}
}

class User(BaseModel):
    name: str
    role: str

@app.get("/")
def home():
    return {"message": "Day 5 - HTTP Exception Handling is Working! 🚀", "docs": "/docs"}

# 1. 200 - OK + 404 - Not Found
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return fake_db[user_id]

# 2. 201 - Created + 400 - Bad Request
@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    if len(user.name) < 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Name should be at least 3 characters long"
        )
    new_id = max(fake_db.keys()) + 1
    fake_db[new_id] = {"id": new_id, **user.dict()}
    return {"message": "User created successfully", "data": fake_db[new_id]}

# 3. 401 - Unauthorized
@app.get("/secure-data/")
def get_secure_data(token: str = None):
    if token != "mysecrettoken123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token. Unauthorized access!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"secret": "This is top secret data!"}

# 4. 403 - Forbidden
@app.get("/admin/")
def get_admin_panel(is_admin: bool = False):
    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to access admin panel"
        )
    return {"message": "Welcome Admin!"}

# 5. 409 - Conflict (Duplicate)
@app.post("/register/")
def register_user(user: User):
    for u in fake_db.values():
        if u["name"].lower() == user.name.lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with name '{user.name}' already exists"
            )
    return {"message": f"User {user.name} registered"}

# 6. 422 - Unprocessable Entity (Auto handled by FastAPI) + Custom 500
@app.get("/error-test/")
def test_server_error(should_fail: bool = False):
    try:
        if should_fail:
            raise ValueError("Something went wrong in DB!")
        return {"message": "Server is fine"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}"
        )

# 7. Custom Exception Handler Example
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "Invalid ID",
                "suggestion": "ID should start from 1",
                "code": "INVALID_ID_0"
            }
        )
    return {"item_id": item_id, "name": "Sample Item"}