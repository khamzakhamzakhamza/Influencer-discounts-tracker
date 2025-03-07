import os
import pytest
from fastapi.testclient import TestClient
from idt_api.infrastructure.dependencies import get_influencer_repository, get_influencer_scanner, get_user_repository
from idt_api.main import app
from tests.component.mock_repositories.mock_influencer_repository import MockInfluencerRepository
from tests.component.mock_repositories.mock_user_repository import MockUserRepository
from tests.component.mock_scanners.mock_influencer_scanner import MockInfluencerScanner

os.environ["ENVIRONMENT"] = "testing"

@pytest.fixture
def client():
     app.state.user_repository = MockUserRepository()
     app.dependency_overrides[get_user_repository] = lambda: app.state.user_repository

     app.state.influencer_repository = MockInfluencerRepository()
     app.dependency_overrides[get_influencer_repository] = lambda: app.state.influencer_repository
     app.state.influencer_scanner = MockInfluencerScanner()
     app.dependency_overrides[get_influencer_scanner] = lambda: app.state.influencer_scanner
     
     return TestClient(app)
