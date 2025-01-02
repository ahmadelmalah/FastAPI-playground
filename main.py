import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from auth.hash_password import HashPassword
import sys

app = FastAPI()

in_memory_db = []


@app.get("/")
def read_root():
    return "Root"


@app.get("/password-hash")
def read_test():
    password = "test"
    hashed_password = HashPassword().hash_password(password)
    res = {}
    res["password"] = password
    res["hashed_password"] = hashed_password
    res["verify_password"] = HashPassword().verify_password(password, hashed_password)
    return res


# Basic Auth with username and password
@app.get("/auth")
def get_user(creds: HTTPBasicCredentials = Depends(HTTPBasic())):
    return {"username": creds.username, "password": creds.password}


# Exception handling
@app.get("/exception")
def get_exeption():
    raise HTTPException(status_code=401, detail="Something went wrong!")


@app.get("/list")
def get_db():
    return in_memory_db


@app.get("/search")
def post_db(item: str):
    return item in in_memory_db


class Item(BaseModel):
    item: str


@app.post("/add")
def post_db(item: Item):
    in_memory_db.append(item.item)
    return item.item


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    uvicorn.run("main:app", reload=True)
