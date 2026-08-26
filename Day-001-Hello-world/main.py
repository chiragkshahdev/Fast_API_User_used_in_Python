from fastapi import FastAPI

app = FastAPI(
    title = "Day 1 - Hello World API", 
    description = "100 Days of FASTAPI Challenge",
    Version = "1.0.0"
)

@app.get("/")
def home():
    return {
        "Day": 1,
        "Topic": "Hello World",
        "Message": "Welcome to 100 Days of FASTAPI!",
        "Docs": "/Docs"
    }

@app.get("/Hello/{name}")
def greet(name: str):
    return{"Message": f"Hello {name}, Day 1 Done!"}

app.get("/Health")
def Health_Check():
    return{"Status": "Ok"}