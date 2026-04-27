import io

from src.main import *
from fastapi import FastAPI
from pydantic import BaseModel
from unittest.mock import patch
import pytest



@pytest.mark.asyncio
async def teste_root():
    result = await root()
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def teste_funcaoteste():
    with patch('random.randint', return_value=1233):
        result = await funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 1233}


@pytest.mark.asyncio
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,50)}




@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="marco", curso="curso 1", ativo=False)
    result = await create_estudante(estudante_teste)

    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudantes_negativo():
    result = await update_estudantes(-5)

    assert not result

@pytest.mark.asyncio
async def test_update_estudantes_positivo():
    result = await update_estudantes(10)

    assert result
@pytest.mark.asyncio
async def teste_delete_estudante_negativo():
    result = await delete_estudantes(-5)

    assert not result
@pytest.mark.asyncio
async def teste_delete_estudante_positivo():
    result = await delete_estudantes(10)

    assert result

