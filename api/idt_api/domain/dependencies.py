from fastapi import Depends
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface
from idt_api.domain.services.user_service import UserService
from idt_api.infrastructure.dependencies import get_user_repository

def get_user_service(user_repo: UserRepositoryInterface = Depends(get_user_repository)):
    return UserService(user_repo)
