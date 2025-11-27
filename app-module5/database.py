from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the database URL from .env (SQLite by default)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

# Required for SQLite
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args=connect_args
)

# Create tables on startup
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency: get a DB session
def get_session():
    with Session(engine) as session:
        yield session
