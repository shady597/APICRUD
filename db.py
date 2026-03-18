from sqlalchemy import String, create_engine, func, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os


DATABASE_URL = "postgresql://postgres:$Hadyla5@localhost:5432/mydatabase"
  
engine  = create_engine(DATABASE_URL)
Sessionlocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        