from sqlalchemy.orm import Session
from . import models, schemas

def get_users(db: Session):
  users = db.query(models.User).all()
  return users