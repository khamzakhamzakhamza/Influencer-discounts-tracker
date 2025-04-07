from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.entities.content import Content

class AffiliatedLinkRepositoryInterface(ABC):
    @abstractmethod
    def save_links(self, content: Content, links: List[AffiliatedLink]):
        pass
