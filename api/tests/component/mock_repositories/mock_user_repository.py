from typing import Optional
from idt_api.domain.entities.user import User
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface

class MockUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = {}

    async def create_user(self, user: User) -> None:
        self.users[user.username] = user

    async def get_user(self, username: str) -> Optional[User]:
        return self.users.get(username)