from .modules import model, view, controller
from fastapi import FastAPI

app = FastAPI()
model = model.Model()

async def root():
    return {"message": "Hello World"}

@app.get("/text/uppercase")
async def root(source):
    upper = model.modify_inputs(source)
    return {"message": upper}

@app.get("/text/palindrome")
async def root(source):
    palindrome = model.is_palindrome(source)
    if palindrome:
        return {"reponse": f"Yes, {source} is {source[::-1]} backwards, a real palindrome "}
    else:
        return {"reponse": f"No, {source} is not a palindrome"}