from abc import ABC, abstractmethod
from scrapper.idt_scrapper.domain.entities.influencer import Influencer

class InfluencerScannerInterface(ABC):
    @abstractmethod
    def rescan_influencer(self, influencer: Influencer):
        pass
