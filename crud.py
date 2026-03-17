import db, schemas
from sqlalchemy.orm import Session  
from sqlalchemy import or_

def create_user(db: Session, user: schemas.Usercreate):
    newuser = db.User(email=user.email, name=user.name)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

def get_user(db: Session, user_id: int):
    return db.query(db.User).filter(db.User.id == user_id).first()

def get_users_byemail(db: Session, email: str):
    return db.query(db.User).filter(db.User.email == email).all()
