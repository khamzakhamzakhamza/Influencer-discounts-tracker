import pytest
from fastapi.testclient import TestClient
from idt_api.main import app

@pytest.fixture
def client():
     return TestClient(app)
