from datetime import datetime, timedelta, timezone
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from tests.shared.builders.influencer_builder import InfluencerBuilder

class MockInfluencerRepository(InfluencerRepositoryInterface):
    __influencers = [
        InfluencerBuilder().with_last_update_date(datetime.now(timezone.utc) - timedelta(days=1)).build(),
        # InfluencerBuilder().with_last_update_date(datetime.now(timezone.utc) - timedelta(days=1)).build(),
        # InfluencerBuilder().with_last_update_date(datetime.now(timezone.utc) - timedelta(days=1)).build(),
    ]
    def get_influencers_by_desc_update_date(self, count: int = 100) -> List[Influencer]:        
        return self.__influencers
    
    def update_influencer(self, influencer: Influencer):
        for i, existing_influencer in enumerate(self.__influencers):
            if existing_influencer.channel_id == influencer.channel_id:
                self.__influencers[i] = influencer
                break
