from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_read_2_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}


# Nuevo test


def test_get_product():
    response = client.get("/products/123?category=electronics")
    assert response.status_code == 200
    assert response.json() == {"product_id": 123, "Categoria": "electronics"}
