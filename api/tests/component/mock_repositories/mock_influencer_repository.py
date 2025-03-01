from typing import Optional
from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface

class MockInfluencerRepository(InfluencerRepositoryInterface):
    def __init__(self):
        self.influencers = {}

    async def get_influencer(self, username: str) -> Optional[Influencer]:
        return self.influencers.get(username)
    
    async def create_influencer(self, influencer: Influencer) -> None:
        self.influencers[influencer.username] = influencer
    
    async def associate_user(self, influencer: Influencer, user: User) -> None:
        return