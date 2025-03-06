from abc import ABC, abstractmethod
from typing import Optional
from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User

class InfluencerRepositoryInterface(ABC):
    @abstractmethod
    def get_influencer(self, channel_id: str) -> Optional[Influencer]:
        pass
    
    @abstractmethod
    def create_influencer(self, influencer: Influencer) -> None:
        pass
    
    @abstractmethod
    def associate_user(self, influencer: Influencer, user: User) -> None:
        pass
