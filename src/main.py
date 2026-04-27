import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 50)}


def create_estudante():
    return Estudante(name="marco", curso="curso 1", ativo=False)


def update_estudantes(id_estudante):
    return id_estudante > 0


def delete_estudantes(id_estudante):
    return id_estudante > 0