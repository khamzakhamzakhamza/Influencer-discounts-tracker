from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.promo import Promo

class PromoRepositoryInterface(ABC):
    @abstractmethod
    def save_promos(self, promo: List[Promo]):
        pass
