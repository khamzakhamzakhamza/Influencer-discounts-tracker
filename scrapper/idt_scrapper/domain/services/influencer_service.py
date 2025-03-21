from datetime import date, datetime, timezone
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface

class InfluencerService:
    def __init__(self, influencer_repository: InfluencerRepositoryInterface, influencer_scanner: InfluencerScannerInterface):
        self._influencer_repository = influencer_repository
        self._influencer_scanner = influencer_scanner

    # TODO: test this shit 
    def get_influencers_to_update(self) -> List[Influencer]:
        influencers = self._influencer_repository.get_influencers_by_desc_update_date()

        today = datetime.now(timezone.utc).date()
        
        return [influencer for influencer in influencers if self.get_last_update_date(influencer) != today]
    
    def update_influencer(self, influencer: Influencer):
        self._influencer_scanner.rescan_influencer(influencer)
        self._influencer_repository.update_influencer(influencer)

    def get_last_update_date(self, influencer: Influencer) -> date:
        if influencer.last_update_date is None:
            return date.min
        
        return influencer.last_update_date.date()
