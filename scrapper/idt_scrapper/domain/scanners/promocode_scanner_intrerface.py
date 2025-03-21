from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content

class PromocodeScannerInterface(ABC):
    @abstractmethod
    def scan_content(self, influencer: Influencer) -> List[Content]:
        pass
