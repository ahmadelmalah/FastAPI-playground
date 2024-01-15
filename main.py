import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

in_memory_db = []

@app.get("/")
def read_root():
    return "Root"

# Basic Auth with username and password
@app.get("/auth")
def get_user(creds: HTTPBasicCredentials = Depends(HTTPBasic())):
    return {"username": creds.username, "password": creds.password}

# Exception handling
@app.get("/exception")
def get_exeption():
    raise HTTPException(status_code=401, detail="Something went wrong!")

@app.get("/db")
def get_db():
    return in_memory_db

@app.post("/db")
def post_db(item: str):
    in_memory_db.append(item)
    return in_memory_db

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)