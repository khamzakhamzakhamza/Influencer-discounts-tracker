from abc import ABC, abstractmethod
import datetime
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content

class ContentScannerInterface(ABC):
    @abstractmethod
    def scan_content(self, influencer: Influencer,  cutoff_date: datetime) -> List[Content]:
        pass
