from fastapi import APIRouter, Depends
from idt_api.api.v1.requests.post_influencer_request import PostInfluencerRequest
from idt_api.domain.dependencies import get_user_service
from idt_api.domain.services.user_service import UserService

router = APIRouter()

@router.post("/influencer")
def post_influencer(request: PostInfluencerRequest, service: UserService = Depends(get_user_service)):
    return service.retrive_or_create_user(request.username)
