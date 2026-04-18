import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste22")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,50)}



@app.get("/teste11")
async def root():
    return {"message": "Olá, mundo!"}

@app.get("/teste3gbb")
async def root():
    return {"message": "Bonjour le monde!"}
