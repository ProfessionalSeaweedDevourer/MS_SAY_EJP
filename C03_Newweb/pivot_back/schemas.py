from pydantic import BaseModel
from datetime import date
from typing import Optional

# 회원가입 요청 스키마
class UserCreate(BaseModel):
    id: str
    password: str
    birth_date: Optional[date] = None
    address: Optional[str] = None

# 응답용 스키마
class UserResponse(BaseModel):
    id: str
    message: str

    class Config:
        from_attributes = True