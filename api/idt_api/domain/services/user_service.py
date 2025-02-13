from idt_api.domain.entities.user import User
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface

class UserService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
    
    def retrive_or_create_user(self, username: str) -> User:
        user = self.user_repository.get_user(username)

        if user:
            return user

        user = User(username)
        
        self.user_repository.create_user(user)
        
        return user
