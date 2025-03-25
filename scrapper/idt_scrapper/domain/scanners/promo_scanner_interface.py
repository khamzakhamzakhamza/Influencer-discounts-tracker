from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.entities.promo import Promo

class PromoScannerInterface(ABC):
    @abstractmethod
    def scan_promos(self, content: List[Content]) -> List[Promo]:
        pass