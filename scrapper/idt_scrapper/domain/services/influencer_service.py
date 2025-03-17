from typing import List
from scrapper.idt_scrapper.domain.entities.influencer import Influencer
from scrapper.idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from scrapper.idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface

class InfluencerService:
    def __init__(self, influencer_repository: InfluencerRepositoryInterface, influencer_scanner: InfluencerScannerInterface):
        self.influencer_repository = influencer_repository
        self.influencer_scanner = influencer_scanner

    def get_influencers_to_update(self) -> List[Influencer]:
        return self.influencer_repository.get_influencer_by_desc_update_date()
    
    def update_influencer(self, influencer: Influencer):
        influencer = self.influencer_scanner.scan_influencer(influencer)
        self.influencer_repository.update_influencer(influencer)
