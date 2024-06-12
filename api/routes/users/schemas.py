from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
  nome: str
  email: str
  data_nascimento: date
  phone: str

  class Config:
    orm_mode = True


  