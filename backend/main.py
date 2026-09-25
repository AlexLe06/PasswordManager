from fastapi import FastAPI, Depends, HTTPException
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
    existing_user = crud.get_user(db, user.user)
    existing_email = crud.get_user(db, user.email)

    if existing_user:
        raise HTTPException(status_code=409, detail="This username is already taken")
    if existing_email:
            raise HTTPException(status_code=409, detail="This email is already used")

    return crud.create_user(db, user)

@app.get("/users")
def get_user():
    pass


if __name__ == "__main__":

    import uvicorn
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload=True)
    
    

