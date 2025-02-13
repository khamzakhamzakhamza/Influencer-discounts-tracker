from idt_api.domain.entities.user import User
from typing import Optional
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface

class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = {}

    def create_user(self, user: User) -> None:
        self.users[user.username] = user

    def get_user(self, username: str) -> Optional[User]:
        return self.users.get(username)
