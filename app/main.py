## ⚙️ Module 4 — Project Structure & Validation
from fastapi import FastAPI
from .models import User
from .database import lifespan
from .routes.users import router as users_router

app = FastAPI(lifespan=lifespan)

app.include_router(users_router)

@app.get("/")
def get_root():
    return {"Message": "Hello World! This is a FastAPI App"}

@app.get("/hello/{name}")
def greet_user(name):
    return {"Welcome": name}

@app.get("/search")
def search(q: str | None = None):
    return {"search results": q}

"""
Things needed to add 
not being able to add users with pre existing id , email or user name
fix the problem of the user_id not auto incremeting when created
fix the problem that the user_id is not being updated when modifying it (model_dump returns all field even if a field is not gonna be updated)
"""