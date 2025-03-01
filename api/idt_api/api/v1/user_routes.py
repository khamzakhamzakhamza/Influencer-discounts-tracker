from fastapi import APIRouter, Depends
from idt_api.api.v1.requests.post_user_request import PostUserRequest
from idt_api.domain.dependencies import get_user_service
from idt_api.domain.services.user_service import UserService

router = APIRouter()

@router.post("/users")
async def post_user(request: PostUserRequest, userService: UserService = Depends(get_user_service)):
    return await userService.retrive_or_create_user(request.username)
