from sqlalchemy import Column, String, Date, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
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
    # store profile image filename (on filesystem) and mime type
    profile_image_filename = Column(String(255), nullable=True)
    profile_image_mime = Column(String(100), nullable=True)
    post_count = Column(Integer, nullable=False, default=0)
    comment_count = Column(Integer, nullable=False, default=0)

    # relationships
    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='author')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(String(36), primary_key=True)
    author_id = Column(String(50), ForeignKey('users.id'))
    content = Column(Text, nullable=False)
    created_at = Column(String(50))
    # relationship to comments
    comments = relationship('Comment', back_populates='post')
    author = relationship('User', back_populates='posts')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(String(36), primary_key=True)
    post_id = Column(String(36), ForeignKey('posts.id'))
    author_id = Column(String(50), ForeignKey('users.id'))
    content = Column(Text, nullable=False)
    created_at = Column(String(50))
    # relationships
    author = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')