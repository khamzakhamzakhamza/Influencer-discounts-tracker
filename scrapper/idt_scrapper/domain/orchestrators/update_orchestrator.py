from typing import List
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.domain.services.promo_service import PromoService

class UpdateOrchestrator:
    def __init__(self, influencer_service: InfluencerService, content_service: ContentService, promo_service: PromoService):
        self._influencer_service = influencer_service
        self._content_service = content_service
        self._promo_service = promo_service

    def update_influencers(self) -> List[str]:
        influencers = self._influencer_service.get_influencers_to_update()
        updated_id = []
        failed_id = []

        for influencer in influencers:
            try:
                self._influencer_service.update_influencer(influencer)

                most_recent_content_date = self._content_service.delete_stale(influencer)
                content = self._content_service.save_content(influencer, most_recent_content_date)
                
                self._promo_service.extract_promos(content)
                
                updated_id.append(influencer.id)
            except Exception as e:
                failed_id.append(influencer.id)
                #TODO Log error

        # TODO: Figure out what to do with failed ones 
        return updated_id
