from abc import ABC, abstractmethod
from idt_api.domain.entities.influencer import Influencer

class InfluencerScannerInterface(ABC):
    @abstractmethod
    def scan_channel_id(self, link: str) -> str:
        pass
    
    @abstractmethod
    def scan_influencer(self, channel_id: str) -> Influencer:
        pass
