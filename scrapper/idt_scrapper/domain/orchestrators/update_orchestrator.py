from typing import List
from scrapper.idt_scrapper.domain.services.influencer_service import InfluencerService
from scrapper.idt_scrapper.domain.services.promocode_service import PromocodeService

class UpdateOrchestrator:
    def __init__(self, influencer_service: InfluencerService, promocode_service: PromocodeService):
        self.influencer_service = influencer_service
        self.promocode_service = promocode_service

    def update_influencers(self) -> List[str]:
        influencers = self.influencer_service.get_influencers_to_update()
        
        updated_id = []

        for influencer in influencers:
            self.influencer_service.update_influencer(influencer)
            self.promocode_service.delete_stale(influencer)
            self.promocode_service.save_promocodes(influencer)
            updated_id.append(influencer.id)

        return updated_id
