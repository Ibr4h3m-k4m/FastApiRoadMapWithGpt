from ..database import users
from ..models import *
from fastapi import APIRouter, HTTPException , Depends

router = APIRouter(prefix="/users", tags=["Users"])


async def get_user_or_404(user_id: int):
    for user in users:
        if user.user_id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/")
async def get_users():
    return [user.model_dump() for user in users]

@router.post("/")
async def add_user(user : User):
    for u in users:
        if u.email == user.email:
            raise HTTPException(status_code=404, detail="Email already exists")
    for u in users:
        if u.name == user.name:
            raise HTTPException(status_code=404, detail="User name already exists")
    if users:
        max_id = max(u.user_id for u in users)
        user.user_id = max_id + 1
    else:
        user.user_id = 1
        
        new_user = User(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            age=user.age
        )
    users.append(new_user)
    return new_user.model_dump()

@router.get("/{user_id}")
async def get_user(user :User= Depends(get_user_or_404)):
    return user

@router.put("/{user_id}")
async def update_user(user_id: int,user_data: UserUpdate,existing_user = Depends(get_user_or_404)):
    # Check if email or name already exist for another user
    for u in users:
        if u.user_id != user_id:
            if u.email == user_data.email:
                raise HTTPException(status_code=400, detail="Email already exists")
            if u.name == user_data.name:
                raise HTTPException(status_code=400, detail="Username already exists")
    # Update the existing user
    existing_user.name = user_data.name
    existing_user.email = user_data.email
    existing_user.age = user_data.age

    return existing_user.model_dump()

@router.patch("/{user_id}")
async def patch_user(user_id: int, user_update: UserUpdate ,user :User= Depends(get_user_or_404) ):
    if user_update .email is not None:
        for u in users:
            if u.user_id != user_id and u.email == user_update.email:
                raise HTTPException(status_code=400, detail="Email already exists")
        user.email = user_update.email
        
    if user_update.name is not None:
        for u in users:
            if u.user_id != user_id and u.name == user_update.name:
                raise HTTPException(status_code=400, detail="User name already exists")
        user.name = user_update.name   
    if user_update.age is not None:
        user.age = user_update.age  
    return user.model_dump()

@router.delete("/{user_id}")
async def delete_user( user_id :int ,user :User= Depends(get_user_or_404)):
        users.remove(user)
        return {"message": "User deleted successfully", "user": user.model_dump()}   

"""
@router.get("/{user_id}")
async def get_user(user_id:int):
    for user in users:
        if user.user_id == user_id:
            return user.model_dump()
    raise HTTPException(status_code=404, detail="User not found")
    
@router.put("/{user_id}")
async def update_user(user_id: int , user : User):
        for user_in_list in users:
            if user_in_list.user_id == user_id:
                for u in users:
                    if u.user_id != user_id:
                        if u.email == user.email:
                            raise HTTPException(status_code=404, detail="Email already exists")
                        if u.name == user.name:
                            raise HTTPException(status_code=404, detail="User name already exists")                
                user_in_list.name = user.name
                user_in_list.email = user.email
                user_in_list.age = user.age
                
                return user_in_list.model_dump()
            
        raise HTTPException(status_code=404, detail="User not found")

@router.patch("/{user_id}")
async def patch_user(user_id: int, user_update: UserUpdate):
    for user_in_list in users:
        if user_in_list.user_id == user_id:

            # EMAIL validation
            if user_update.email is not None:
                for u in users:
                    if u.user_id != user_id and u.email == user_update.email:
                        raise HTTPException(status_code=400, detail="Email already exists")
                user_in_list.email = user_update.email

            # NAME validation
            if user_update.name is not None:
                for u in users:
                    if u.user_id != user_id and u.name == user_update.name:
                        raise HTTPException(status_code=400, detail="User name already exists")
                user_in_list.name = user_update.name

            # AGE update (no validation)
            if user_update.age is not None:
                user_in_list.age = user_update.age

            return user_in_list.model_dump()

    raise HTTPException(status_code=404, detail="User not found")
 


@router.delete("/{user_id}")
async def delete_user(user_id: int):
        for user_in_list in users:
            if user_in_list.user_id == user_id:
                users.remove(user_in_list)
                return user_in_list.model_dump()
        return {"error": "User not found"}   
   
"""
   


                

   
