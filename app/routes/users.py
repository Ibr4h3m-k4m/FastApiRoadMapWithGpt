from ..database import users
from ..models import User
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users():
    return [user.model_dump() for user in users]

@router.get("/{user_id}")
async def get_user(user_id:int):
    for user in users:
        if user.user_id == user_id:
            return user.model_dump()
    return {"error": "User not found"}
   
   
@router.post("/")
async def add_user(user : User):
    users.append(user)
    return user.model_dump()

                
@router.put("/{user_id}")
async def update_user(user_id: int , user : User):
        for user_in_list in users:
            if user_in_list.user_id == user_id:
                user_in_list.name = user.name
                user_in_list.email = user.email
                user_in_list.age = user.age
                
                return user_in_list.model_dump()

                
            
        return {"error": "User not found"}


@router.delete("/{user_id}")
async def delete_user(user_id: int):
        for user in users:
            if user.user_id == user_id:
                users.remove(user)
                return user.model_dump()
        return {"error": "User not found"}   
   