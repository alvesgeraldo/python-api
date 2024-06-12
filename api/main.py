from fastapi import FastAPI
from routes.users import user as user_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def hello():
  return {"message": "Hello"}

app.include_router(user_router.router, prefix="/users", tags=["users"])