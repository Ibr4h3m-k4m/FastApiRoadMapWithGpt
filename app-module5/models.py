from pydantic import EmailStr
from sqlmodel import Field, SQLModel , Column, String
from typing import Optional

    
class User(SQLModel, table=True):
    user_id : Optional[int] = Field(default=None, primary_key=True)
    name : str
    email : EmailStr = Field(sa_column=Column(String,unique=True,nullable=False))
    age : int
    

class UserUpdate(SQLModel , table=False):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    