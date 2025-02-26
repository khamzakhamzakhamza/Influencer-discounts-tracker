from abc import ABC, abstractmethod
from idt_api.domain.entities.influencer import Influencer

class InfluencerScannerInterface(ABC):
    @abstractmethod
    def scan_username(self, link: str) -> str:
        pass
    
    @abstractmethod
    def scan_influencer(self, link: str) -> Influencer:
        pass
