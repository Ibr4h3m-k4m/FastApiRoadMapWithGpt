from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_db_and_tables
from routes import users  # make sure routes is a package with __init__.py


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic: create database tables
    create_db_and_tables()

    yield

    # Shutdown logic: optional (e.g., dispose engine)
    # from database import engine
    # engine.dispose()


app = FastAPI(
    title="My FastAPI App",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])


# Root endpoint
@app.get("/", tags=["Root"])
def home():
    return {"message": "Welcome to the FastAPI Application!"}


# Example greeting endpoint
@app.get("/hello/{name}", tags=["Utilities"])
def greet_user(name: str):
    return {"Welcome": name}


# Example search endpoint with optional query parameter
@app.get("/search", tags=["Utilities"])
def search(q: str | None = None):
    return {"search results": q}
