from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Password Vault API"}

@app.get("/hello/{name}")
async def say_hello(name: str):

    return {"message": f"Hello {name}"}

@app.post("/users")
async def create_user():
    
    
    return user


if __name__ == "__main__":

    import uvicorn
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload=True)
    
    

