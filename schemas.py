from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    class Config:
        from_attributes = True  # orm_mode in Pydantic v1

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    posts: List[Post] = []
    
    class Config:
        from_attributes = True