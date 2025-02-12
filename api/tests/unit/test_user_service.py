from idt_api.domain.services.user_service import UserService

def retrive_or_create_user_should_call_dependencies():
    username = "John Doe"
    service = UserService()

    user = service.retrive_or_create_user(username)
    
    assert user is not None
    assert user.username == username
    assert user.id == 1
