from abc import ABC, abstractmethod
from typing import List
from scrapper.idt_scrapper.domain.entities.promocode import Promocode

class PromocodeRepositoryInterface(ABC):
    @abstractmethod
    def delete_promocodes(self, promocode_ids: List[str]):
        pass

    @abstractmethod
    def create_promocodes(self, promocodes: List[Promocode]):
        pass