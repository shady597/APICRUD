from sqlalchemy import String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer
from dotenv import load_dotenv
import os


DATABASE_URL  = os.getenv("DATABASE_URL")
  
engine  = create_engine(DATABASE_URL)
Sessionlocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class usertable(Base):
    __tablename__ = "newtable"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class newposts(Base):
    __tablename__ = "newposts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)