import db, schemas
from sqlalchemy.orm import Session  
from sqlalchemy import or_
from db import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users_byemail(db: Session, email: str):
    return db.query(User).filter(User.email == email).all()
