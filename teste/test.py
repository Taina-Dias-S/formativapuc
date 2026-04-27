import io

from src.main import *
from fastapi import FastAPI
from pydantic import BaseModel
from unittest.mock import patch

def teste_root():
    assert root() == {"message": "Hello World"}

def teste_funcaoteste():
    with patch('random.randint', return_value=1233):
       result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 1233}



def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,50)}





def test_create_estudante():
    estudante_teste = Estudante(name="marco", curso="curso 1", ativo=False)
    assert estudante_teste == create_estudante()


def test_update_estudantes_negativo():
    assert not update_estudantes(-5)

def test_update_estudantes_positivo():
        assert update_estudantes(10)


def teste_delete_estudante_negativo():
    assert not delete_estudantes(-5)

def teste_delete_estudante_positivo():
    assert  delete_estudantes(10)

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool