from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str   
    phone_no: Optional[str] = None   


class UserResponse(BaseModel):
    user_id: int
    email: str