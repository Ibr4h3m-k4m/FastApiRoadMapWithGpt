from fastapi import FastAPI

from pydantic import BaseModel , EmailStr
app = FastAPI()

class User(BaseModel):
    user_id : int 
    name : str
    email : EmailStr
    age : int


@app.get("/")
def get_root():
    return {"Message" : "Hello World! This is a FastAPI App"}


@app.get("/hello/{name}")
def greet_user(name):
    return {"Welcome" : name}

@app.get("/search")
def search(q : str | None = None):
    return {"search results" : q}
    

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.post("/users")
def add_users(user : User):
    return {"user_id": user.user_id , "name" : user.name ,"Email" : user.email ,"Age" : user.age }