from pydantic import BaseModel, validator
from datetime import date
from typing import Optional

# 회원가입 요청 스키마
class UserCreate(BaseModel):
    id: str
    password: str
    birth_date: Optional[date] = None
    address: Optional[str] = None

    @validator('birth_date', pre=True)
    def empty_str_to_none(cls, v):
        # Accept empty string from frontend and coerce to None so Optional[date] passes
        if v == "" or v is None:
            return None
        return v

# 응답용 스키마
class UserResponse(BaseModel):
    id: str
    message: str

    class Config:
        from_attributes = True

# 로그인 요청 스키마
class UserLogin(BaseModel):
    id: str
    password: str


# 로그인 응답 스키마 (프론트에서 `name`을 기대할 수 있음)
class LoginResponse(BaseModel):
    id: str
    name: Optional[str] = None
    birth_date: Optional[date] = None
    address: Optional[str] = None
    role: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True


# Settings 업데이트용 스키마
class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True