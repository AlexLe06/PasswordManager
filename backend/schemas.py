from pydantic import BaseModel

class createUser(BaseModel):
    user: str
    email: str
    password: str