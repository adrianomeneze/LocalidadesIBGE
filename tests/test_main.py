from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)


def test_get_distritos_success():
    response_data = [
        {"id": 1, "nome": "Distrito 1"},
        {"id": 2, "nome": "Distrito 2"}
    ]

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = response_data

        response = client.get("/distritos")
        assert response.status_code == 200
        assert response.json() == response_data


def test_get_distritos_order_by():
    response_data = [
        {"id": 1, "nome": "Distrito A"},
        {"id": 2, "nome": "Distrito B"}
    ]

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = response_data

        response = client.get("/distritos", params={"orderBy": "nome"})
        assert response.status_code == 200
        assert response.json() == response_data


def test_get_distritos_view():
    response_data = [
        {"id": 1, "nome": "Distrito X"},
        {"id": 2, "nome": "Distrito Y"}
    ]

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = response_data

        response = client.get("/distritos", params={"view": "nivelado"})
        assert response.status_code == 200
        assert response.json() == response_data


def test_get_distritos_failure():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 500

        response = client.get("/distritos")
        assert response.status_code == 200
        assert response.json() == {"error": "Não foi possível recuperar dados do IBGE"}
