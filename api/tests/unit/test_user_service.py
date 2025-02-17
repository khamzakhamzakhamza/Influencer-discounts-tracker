import pytest
from unittest.mock import MagicMock
from idt_api.domain.entities.user import User
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface
from idt_api.domain.services.user_service import UserService
from tests.shared.utils import is_valid_guid

@pytest.fixture
def user_service():
    mock_repo = MagicMock(spec=UserRepositoryInterface)
    service = UserService(mock_repo)
    return service, mock_repo

def test_retrive_or_create_user_should_return_existing_user(user_service):
    # Arrange
    expected_user = User("John Doe")
    
    service, mock_repo = user_service
    mock_repo.get_user.return_value = expected_user

    # Act
    user = service.retrive_or_create_user(expected_user.username)
    
    # Assert
    assert user is not None
    assert is_valid_guid(user.id) is True
    assert user == expected_user
    mock_repo.get_user.assert_called_once_with(expected_user.username)
    mock_repo.create_user.assert_not_called()

def test_retrive_or_create_user_should_create_new_user(user_service):
    # Arrange
    expected_user = User("John Doe")
    
    service, mock_repo = user_service
    mock_repo.get_user.return_value = None

    # Act
    user = service.retrive_or_create_user(expected_user.username)
    
    # Assert
    assert user is not None
    assert is_valid_guid(user.id) is True
    assert user != expected_user
    mock_repo.get_user.assert_called_once_with(expected_user.username)
    mock_repo.create_user.assert_called_once()