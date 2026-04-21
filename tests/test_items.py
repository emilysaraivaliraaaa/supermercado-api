import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

ITEM_VALIDO = {
    "nome": "Arroz",
    "preco": 25.90,
    "quantidade": 100,
    "categoria": "Grãos",
    "marca": "Urbano",
    "data_validade": "2027-12-31",
    "fornecedor": "Distribuidora ABC"
}


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_criar_item():
    response = client.post("/items", json=ITEM_VALIDO)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == ITEM_VALIDO["nome"]
    assert "id" in data


def test_listar_itens():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_item_por_id():
    criado = client.post("/items", json=ITEM_VALIDO).json()
    response = client.get(f"/items?item_id={criado['id']}")
    assert response.status_code == 200
    assert response.json()[0]["id"] == criado["id"]


def test_atualizar_item():
    criado = client.post("/items", json=ITEM_VALIDO).json()
    response = client.put(f"/items/{criado['id']}", json={"preco": 19.90})
    assert response.status_code == 200
    assert response.json()["preco"] == 19.90


def test_deletar_item():
    criado = client.post("/items", json=ITEM_VALIDO).json()
    response = client.delete(f"/items/{criado['id']}")
    assert response.status_code == 200


def test_item_nao_encontrado():
    response = client.get("/items?item_id=99999")
    assert response.status_code == 404
