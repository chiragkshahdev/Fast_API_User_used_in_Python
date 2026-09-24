# Day 6 - Auto Docs (Swagger & ReDoc) | FastAPI

FastAPI generates documentation automatically. No extra work needed!

### 🔥 What is Auto Docs?

When you create API with FastAPI, it auto-generates 2 beautiful doc pages:

| URL | Name | Use |
| :--- | :--- | :--- |
| `/docs` | Swagger UI | Try APIs directly, best for development |
| `/redoc` | ReDoc | Beautiful reading docs, best for sharing |
| `/openapi.json` | OpenAPI Schema | Raw JSON for other tools |

### ✨ What I Did in Day 6

1. **Custom Title, Description, Version, Contact** in `FastAPI()` object
2. **Tags** - Grouping APIs (Users, Products)
3. **Pydantic Field()** with `example` and `description` - Makes docs interactive
4. **Docstring** inside function -> Shows as description in Swagger
5. **summary, response_description, responses** parameters
6. **Query params with description**

### 📸 Screenshots to Add
Add 2 screenshots in this folder:
- `swagger.png` - Screenshot of /docs
- `redoc.png` - Screenshot of /redoc

### 💡 Key Learnings

- FastAPI uses OpenAPI standard internally
- `Field(..., example="")` is the secret to great docs
- `response_model` automatically shows response structure
- No need for Postman if you have `/docs` - you can test there itself
- Good docs = More GitHub stars

### 🛠️ Tech Stack
- FastAPI
- Pydantic
- Swagger UI (built-in)
- ReDoc (built-in)

### 🚀 How to Run
```bash
uvicorn main:app --reload