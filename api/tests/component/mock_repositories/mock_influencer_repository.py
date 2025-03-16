from typing import List, Optional
from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface

class MockInfluencerRepository(InfluencerRepositoryInterface):
    def __init__(self):
        self.influencers = {}

    async def get_influencer_by_channel_id(self, channel_id: str) -> Optional[Influencer]:
        return self.influencers.get(channel_id)
    
    async def get_influencer_by_id(self, id: str) -> Optional[Influencer]:
        for influencer in self.influencers.values():
            if influencer.id == id:
                return influencer
        
        return None
    
    async def create_influencer(self, influencer: Influencer, user: User) -> None:
        self.influencers[influencer.username] = influencer
    
    async def associate_user(self, influencer: Influencer, user: User) -> None:
        return
    
    async def get_user_influencers(self, user: User) -> List[Influencer]:
        return list(self.influencers.values())
    
    async def disassociate_user_influencer(self, user: User, influencer: Influencer) -> int:
        del self.influencers[influencer.username]

        return 1