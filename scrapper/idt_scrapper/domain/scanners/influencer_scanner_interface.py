from abc import ABC, abstractmethod
from scrapper.idt_scrapper.domain.entities.influencer import Influencer

class InfluencerScannerInterface(ABC):
    @abstractmethod
    def scan_influencer(self, channel_id: str) -> Influencer:
        pass
