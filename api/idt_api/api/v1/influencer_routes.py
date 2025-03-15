from fastapi import APIRouter, Depends
from idt_api.api.v1.requests.post_influencer_request import PostInfluencerRequest
from idt_api.domain.dependencies import get_influencer_service, get_user_service
from idt_api.domain.services.influencer_service import InfluencerService
from idt_api.domain.services.user_service import UserService

router = APIRouter()

@router.post("/influencers")
async def post_influencer(request: PostInfluencerRequest, influencerService: InfluencerService = Depends(get_influencer_service), userService: UserService = Depends(get_user_service)):
    user = await userService.retrive_or_create_user(request.username)
    return await influencerService.create_and_associate_influencer(user, request.link)

@router.get("/influencers")
async def get_influencers(username: str, influencerService: InfluencerService = Depends(get_influencer_service), userService: UserService = Depends(get_user_service)):
    user = await userService.retrive_or_create_user(username)
    return await influencerService.get_user_influencers(user)

@router.delete("/influencers")
async def get_influencers(username: str, influencer_id: str, influencerService: InfluencerService = Depends(get_influencer_service), userService: UserService = Depends(get_user_service)):
    user = await userService.retrive_or_create_user(username)
    return await influencerService.disassociate_user_influencer(user, influencer_id)
