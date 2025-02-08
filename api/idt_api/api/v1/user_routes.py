from fastapi import APIRouter, Depends
from idt_api.domain.services.user_service import UserService

router = APIRouter()

@router.post("/users")
def post_user(username: str, service: UserService = Depends()):
    return service.retrive_or_create_user(username)
