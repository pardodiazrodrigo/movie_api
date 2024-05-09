from fastapi.testclient import TestClient
from fastapi import status
import main

client = TestClient(main.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "server is running"}
