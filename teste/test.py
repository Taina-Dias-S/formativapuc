import io

from src.main import *
from fastapi import FastAPI
from pydantic import BaseModel
from unittest.mock import patch



def teste_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def teste_funcaoteste():
    with patch('random.randint', return_value=1233):
        result = funcaoteste()
    yield result
    assert result == {"teste": True, "num_aleatorio": 1233}



def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,50)}





def test_create_estudante():
    estudante_teste = Estudante(name="marco", curso="curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result


def test_update_estudantes_negativo():
    result = update_estudantes(-5)
    yield result
    assert not result

def test_update_estudantes_positivo():
    result = update_estudantes(10)
    yield result
    assert result

def teste_delete_estudante_negativo():
    result = delete_estudantes(-5)
    yield result
    assert not result

def teste_delete_estudante_positivo():
    result = delete_estudantes(10)
    yield result
    assert result

