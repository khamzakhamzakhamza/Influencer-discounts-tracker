from fastapi import APIRouter, Depends
from idt_api.api.v1.requests.post_user_request import PostUserRequest
from idt_api.domain.services.user_service import UserService

router = APIRouter()

@router.post("/users")
def post_user(request: PostUserRequest, service: UserService = Depends()):
    return service.retrive_or_create_user(request.username)
