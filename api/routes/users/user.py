from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from typing import List
from database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.UserBase])
def get_users(db: Session = Depends(get_db)):
  try:
    return crud.get_users(db=db)
  except:
    HTTPException(status_code=404, detail="Não há registros")