# 🚀 Fast_API_User_used_in_Python

> A 30-Day FastAPI learning series - From Hello World to Production-Ready User APIs.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)]()
[![Status](https://img.shields.io/badge/Learning-In_Progress-orange?style=for-the-badge)]()

### 📖 About
This is my daily hands-on journey to master FastAPI, focusing on **User Management, External API Integration, and Authentication**.
Built by **Chirag Kiran Shah | FYBSc IT - Mumbai University**.

### 🗓️ Daily Progress

| Day | Folder | Topic Covered | Key Concepts |
|-----|--------|---------------|--------------|
| **Day 01** | `Day-001-Hello-world` | Hello World & Setup | `FastAPI()`, `uvicorn`, `@app.get()` |
| **Day 02** | `Day-002-Working-with-APIs-in-Python` | Consuming External APIs | `httpx`, `requests`, ISS Location API, OpenWeather API, API Keys with `.env` |
| **Day 03** | `Day-003-User-CRUD-Auth` | **User Model, Validation & Dependency** | `Pydantic`, `BaseModel`, `EmailStr`, `Depends()`, `HTTPException` |

### ✨ Day 02 Highlights (Your last commit)
- Fetched real-time ISS position using Open Notify API
- Integrated OpenWeather API with secure API Key handling
- Used `python-dotenv` to hide keys

### 🚀 Getting Started
```bash
# 1. Clone
git clone https://github.com/chiragkshahdev/Fast_API_User_used_in_Python.git

# 2. Create venv
python -m venv venv
venv\Scripts\activate # Windows

# 3. Install
pip install fastapi uvicorn httpx python-dotenv pydantic[email]

# 4. Run any day (example Day 3)
cd Day-003-User-CRUD-Auth
uvicorn main:app --reload
