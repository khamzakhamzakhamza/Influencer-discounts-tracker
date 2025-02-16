from abc import ABC, abstractmethod
from typing import Optional
from idt_api.domain.entities.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, user: User) -> None:
        pass
    
    @abstractmethod
    def get_user(self, username: str) -> Optional[User]:
        pass

