from .models import User
from contextlib import asynccontextmanager
import json
from fastapi import FastAPI

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