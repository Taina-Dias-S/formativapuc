from unittest.mock import patch
import pytest

from src.main import *



@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch("src.main.random.randint", return_value=1233):
        result = await funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 1233}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="marco", curso="curso 1", ativo=False)
    result = await create_estudante()

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
async def test_delete_estudante_negativo():
    result = await delete_estudantes(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudantes(10)
    assert result

@pytest.mark.asyncio
async def test_root_tem_message():
    result = await root()
    assert "message" in result


@pytest.mark.asyncio
async def test_funcaoteste_tem_numero():
    with patch("src.main.random.randint", return_value=10):
        result = await funcaoteste()

    assert result["num_aleatorio"] == 10


@pytest.mark.asyncio
async def test_update_estudantes_zero():
    result = await update_estudantes(0)
    assert not result