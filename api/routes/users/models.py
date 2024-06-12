from sqlalchemy import Column, Integer, String, Date
from database import Base

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String, index=True)
  email = Column(String, index=True)
  data_nascimento = Column(Date)
  phone = Column(String)