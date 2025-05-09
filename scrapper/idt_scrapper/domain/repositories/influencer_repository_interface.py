from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer

class InfluencerRepositoryInterface(ABC):
    @abstractmethod
    def get_influencers_by_desc_update_date(self, count: int = 100) -> List[Influencer]:
        pass

    @abstractmethod
    def update_influencer(self, influencer: Influencer):
        pass
