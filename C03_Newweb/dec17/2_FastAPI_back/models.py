from sqlalchemy import Column, String, Integer
from database import Base

class Menu(Base):
    __tablename__ = "dec17_menu"

    m_name = Column(String(30), primary_key=True)
    m_price = Column(Integer, nullable=False)
    m_desc = Column(String(100), nullable=False)