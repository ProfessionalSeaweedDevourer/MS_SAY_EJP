from sqlalchemy import Column, String, Date, LargeBinary
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True)
    password = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=True)
    address = Column(String(255), nullable=True)
    name = Column(String(100), nullable=True)
    role = Column(String(100), nullable=True)
    description = Column(String(500), nullable=True)
    profile_image = Column(LargeBinary, nullable=True)