from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink

class AffiliatedLinkScannerInterface(ABC):
    @abstractmethod
    def scan_links(self, content: List[Content]) -> List[AffiliatedLink]:
        pass