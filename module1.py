## 🧩 Module 1 — FastAPI Basics
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
    

"""@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
@app.post("/users")
def add_users(user : User):
    return {"user_id": user.user_id , "name" : user.name ,"email" : user.email ,"Age" : user.age }

"""

## 🧰 Module 2 — CRUD Basics
# First create a list to store users 
"""
users: list[User] = []

users model
{
  "user_id": 0,
  "name": "string",
  "email": "user@example.com",
  "age": 0
}


@app.get("/users")
def get_users():
    result = []
    for user in users:
                result.append({
                    "user_id":user.user_id ,
                    "user name":user.name ,
                    "user email":user.email ,
                    "user age":user.age})
    return result
                
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            return {
                "user_id": user.user_id,
                "name": user.name,
                "email": user.email,
                "age": user.age
            }
    return {"error": "User not found"}


@app.post("/users")
def add_users(user : User):
    users.append(user)
    return {"user_id": user.user_id , "name" : user.name ,"email" : user.email ,"Age" : user.age }

                
@app.put("/users/{user_id}")
def update_user(user_id: int , user : User):
        for user_in_list in users:
            if user_in_list.user_id == user_id:
                user_in_list.name = user.name
                user_in_list.email = user.email
                user_in_list.age = user.age
                
                return {"user_id": user_in_list.user_id,
                        "name": user_in_list.name,
                        "email": user_in_list.email,
                        "age": user_in_list.age }

                
            
        return {"error": "User not found"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
        for user in users:
            if user.user_id == user_id:
                users.remove(user)
                return user
        return {"error": "User not found"}"""
    
    
## 🧰 Module 3 — Data Persistance


from contextlib import asynccontextmanager
from fastapi import Request
import json

users: list[User] = []

@asynccontextmanager
async def lifespan(app : FastAPI):
    # load users into a list from the json file
    try:
        with open('users.json','r') as file:
            data = json.load(file)
            for item in data:
                users.append(User(**item)) # dict ot user object using kwargs 
        print("JSON file loaded successfully")
    except FileNotFoundError:
        print("The users.json file doesnt exist")
    except json.JSONDecodeError:
        print("Json file is invalid")
        
    yield
    
    # save users back to the json file on shutdown 
    with open("users.json" , "w") as file:
        json.dump([user.model_dump() for user in users] , file , indent= 1)
    print("JSON file unloaded successfully and app is shuting down")
    

app = FastAPI(lifespan=lifespan)

@app.get("/users")
async def get_users():
    return [user.model_dump() for user in users]

@app.get("/users/{user_id}")
async def get_user(user_id:int):
    for user in users:
        if user.user_id == user_id:
            return user.model_dump()
    return {"error": "User not found"}
   
   
@app.post("/users")
async def add_user(user : User):
    users.append(user)
    return user.model_dump()

                
@app.put("/users/{user_id}")
async def update_user(user_id: int , user : User):
        for user_in_list in users:
            if user_in_list.user_id == user_id:
                user_in_list.name = user.name
                user_in_list.email = user.email
                user_in_list.age = user.age
                
                return user_in_list.model_dump()

                
            
        return {"error": "User not found"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
        for user in users:
            if user.user_id == user_id:
                users.remove(user)
                return user.model_dump()
        return {"error": "User not found"}   
   
   
 
"""
Things needed to add 
not being able to add users with pre existing id , email or user name
fix the problem of the user_id not auto incremeting when created
fix the problem that the user_id is not being updated when modifying it (model_dump returns all field even if a field is not gonna be updated)
"""