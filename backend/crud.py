from sqlalchemy.orm import Session
from . import models, schemas, auth

def create_user(db : Session, user: schemas.createUser):
    password = auth.hash_password(user.password)
    db_user = models.User(username=user.user, email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session):
    pass
