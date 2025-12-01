#Example — Response Model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class UserOut(BaseModel):
    name: str
    age: int

@app.post("/user", response_model=UserOut)
def create_user(user: User):
    return user       # password is automatically removed
