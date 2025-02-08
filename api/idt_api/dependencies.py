from fastapi import Depends
from idt_api.domain.services.user_service import UserService

def get_user_service():
    return UserService()
