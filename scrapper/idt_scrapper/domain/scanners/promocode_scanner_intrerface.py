from abc import ABC, abstractmethod
from typing import List
from scrapper.idt_scrapper.domain.entities.promocode import Promocode

class PromocodeScannerInterface(ABC):
    @abstractmethod
    def scan_promocodes(self, channel_id: str) -> List[Promocode]:
        pass
