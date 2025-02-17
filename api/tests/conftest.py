import os
import pytest
from fastapi.testclient import TestClient
from idt_api.infrastructure.dependencies import get_user_repository
from idt_api.infrastructure.repositories.neo4j_user_repository import Neo4jUserRepository
from idt_api.main import app
from tests.component.mock_repositories.mock_user_repository import MockUserRepository

os.environ["ENVIRONMENT"] = "testing"

@pytest.fixture
def client():
     app.state.user_repository = MockUserRepository()
     app.dependency_overrides[get_user_repository] = lambda: app.state.user_repository
     return TestClient(app)
