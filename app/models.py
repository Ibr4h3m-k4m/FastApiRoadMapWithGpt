from pydantic import BaseModel , EmailStr


class User(BaseModel):
    user_id : int 
    name : str
    email : EmailStr
    age : int
    
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]