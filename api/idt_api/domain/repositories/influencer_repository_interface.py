from abc import ABC, abstractmethod
from typing import List, Optional
from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User

class InfluencerRepositoryInterface(ABC):
    @abstractmethod
    def get_influencer_by_channel_id(self, channel_id: str) -> Optional[Influencer]:
        pass

    @abstractmethod
    def get_influencer_by_id(self, influencer_id: str) -> Optional[Influencer]:
        pass
    
    @abstractmethod
    def create_influencer(self, influencer: Influencer) -> None:
        pass
    
    @abstractmethod
    def associate_user(self, influencer: Influencer, user: User) -> None:
        pass

    @abstractmethod
    def get_user_influencers(self, user: User) -> List[Influencer]:
        pass

    @abstractmethod
    def disassociate_user_influencer(self, user: User, influencer: Influencer) -> int:
        pass
