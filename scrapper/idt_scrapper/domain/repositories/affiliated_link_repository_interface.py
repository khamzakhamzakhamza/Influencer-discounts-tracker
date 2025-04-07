from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.entities.promo import Promo

class AffiliatedLinkRepositoryInterface(ABC):
    @abstractmethod
    def save_links(self, links: List[AffiliatedLink]) -> List[Promo]:
        pass
