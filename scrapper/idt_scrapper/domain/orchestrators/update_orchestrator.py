from typing import List
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.promocode_service import PromocodeService

class UpdateOrchestrator:
    def __init__(self, influencer_service: InfluencerService, promocode_service: PromocodeService):
        self._influencer_service = influencer_service
        self._promocode_service = promocode_service

    def update_influencers(self) -> List[str]:
        influencers = self._influencer_service.get_influencers_to_update()
        
        updated_id = []
        failed_id = []

        for influencer in influencers:
            try:
                self._influencer_service.update_influencer(influencer)
                # self._promocode_service.delete_stale(influencer)
                self._promocode_service.save_promocodes(influencer)
                updated_id.append(influencer.id)
            except Exception as e:
                failed_id.append(influencer.id)
                #TODO Log error

        # TODO: Figure out what to do with failed ones 
        return updated_id
