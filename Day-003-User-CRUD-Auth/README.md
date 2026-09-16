# Day 003 - Working with User Model, Validation & Dependency Injection

### 🎯 Objective
Today we moved from external APIs to our own **User Management System**. This is the core of any backend.

### 💡 What I Learned
1. **Pydantic Validation:** Using `EmailStr` and `Field` to auto-validate user input. No need for manual if-else.
2. **Request vs Response Model:** `UserCreate` contains password, but `UserOut` hides it. Best practice for security.
3. **Dependency Injection `Depends()`:** Created `get_current_user_validation()` to check duplicate email before creating user. This is how real auth works.
4. **HTTPException:** Proper error handling with 400, 404.

### 🧪 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users` | Create new user with validation |
| GET | `/users` | Get all users |
| GET | `/users/{id}` | Get user by ID |

### ▶️ How to Test
```bash
uvicorn main:app --reload