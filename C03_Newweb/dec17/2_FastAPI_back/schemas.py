from pydantic import BaseModel

class MenuBase(BaseModel):
    m_name: str
    m_price: int
    m_desc: str

class MenuCreate(MenuBase):
    pass

class MenuRead(MenuBase):
    class Config:
        from_attributes = True