from idt_api.domain.services.user_service import UserService
from tests.shared.utils import is_valid_guid

def test_retrive_or_create_user_should_call_dependencies():
    username = "John Doe"
    service = UserService()

    user = service.retrive_or_create_user(username)
    
    assert user is not None
    assert user.username == username
    assert is_valid_guid(user.id) is True
