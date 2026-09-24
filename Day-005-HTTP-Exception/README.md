# Day 5 - HTTP Exception Handling | FastAPI | Python

Learn how to handle different HTTP status codes professionally in FastAPI.

### 🚀 Live Docs
After running, open: `http://127.0.0.1:8000/docs`

### 📚 HTTP Status Codes Covered

| Code | Name | When to Use | Example in Code |
| :--- | :--- | :--- | :--- |
| 200 | OK | Data fetched successfully | `GET /users/{id}` |
| 201 | Created | New resource created | `POST /users/` |
| 400 | Bad Request | Invalid input | Name < 3 chars |
| 401 | Unauthorized | Missing/Wrong token | `/secure-data/` |
| 403 | Forbidden | No permission | `/admin/` |
| 404 | Not Found | Resource not found | User ID not found |
| 409 | Conflict | Duplicate entry | Same name register |
| 500 | Server Error | Unexpected error | Try-catch block |

### 💡 What I Learned
- `raise HTTPException(status_code, detail)` is the core
- Use `fastapi.status` for clean codes instead of numbers
- How to send custom JSON in `detail`
- Difference between 401 vs 403 vs 404
- Using `headers` for Auth errors

### 🛠️ Tech Stack
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

### 📂 How to Run
```bash
pip install fastapi uvicorn
uvicorn main:app --reload