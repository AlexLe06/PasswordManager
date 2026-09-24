from fastapi import FastAPI, Depends
from . import schemas, crud
from sqlalchemy.orm import Session
from .database import get_db


app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Password Vault API"}

@app.get("/hello/{name}")
async def say_hello(name: str):

    return {"message": f"Hello {name}"}

@app.post("/users")
def create_user(user: schemas.createUser, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


if __name__ == "__main__":

    import uvicorn
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload=True)
    
    

