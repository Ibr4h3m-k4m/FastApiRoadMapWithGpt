from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select, Session
from ..models import User, UserUpdate
from ..database import get_session

router = APIRouter(prefix="/", tags=["Users"])

# Dependency to fetch a user by ID
async def get_user_or_404(user_id: int, session: Session = Depends(get_session)):
    query = select(User).where(User.user_id == user_id)
    user = session.exec(query).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# GET all users
@router.get("/")
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return [user.model_dump() for user in users]

# GET single user
@router.get("/{user_id}")
async def get_user(user: User = Depends(get_user_or_404)):
    return user.model_dump()

# POST new user 
@router.post("/")
async def add_user(user: User, session: Session = Depends(get_session)):
    # Check for duplicate email
    if session.exec(select(User).where(User.email == user.email)).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Check for duplicate name
    if session.exec(select(User).where(User.name == user.name)).first():
        raise HTTPException(status_code=400, detail="Name already exists")
    
    # Add user to the session and commit
    session.add(user)
    session.commit()
    session.refresh(user)  # Refresh to get auto-generated ID
    
    return user.model_dump()


# PUT update user
@router.put("/{user_id}")
async def update_user(user_id: int, user_data: UserUpdate, session: Session = Depends(get_session), existing_user: User = Depends(get_user_or_404)):
    if user_data.email and session.exec(select(User).where((User.email == user_data.email) & (User.user_id != user_id))
).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    if user_data.name and session.exec(select(User).where((User.name == user_data.name) & (User.user_id != user_id))
).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Update fields
    if user_data.name is not None:
        existing_user.name = user_data.name
    if user_data.email is not None:
        existing_user.email = user_data.email
    if user_data.age is not None:
        existing_user.age = user_data.age
    
    session.add(existing_user)
    session.commit()
    session.refresh(existing_user)
    return existing_user.model_dump()


# PATCH partial update
@router.patch("/{user_id}")
async def patch_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_session), user: User = Depends(get_user_or_404)):
    if user_update.email and session.exec(select(User).where((User.email == user_update.email) & (User.user_id != user_id))
).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    if user_update.name and session.exec(select(User).where((User.name == user_update.name) & (User.user_id != user_id))
).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    if user_update.name is not None:
        user.name = user_update.name
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.age is not None:
        user.age = user_update.age

    session.add(user)
    session.commit()
    session.refresh(user)
    return user.model_dump()
        
    

@router.delete("/{user_id}")
async def delete_user(user_id :int , session: Session = Depends(get_session),user :User= Depends(get_user_or_404)):
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully", "user": user.model_dump()}   
