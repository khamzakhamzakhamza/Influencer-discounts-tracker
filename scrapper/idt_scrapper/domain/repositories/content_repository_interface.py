from abc import ABC, abstractmethod
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content

class ContentRepositoryInterface(ABC):
    @abstractmethod
    def get_content(self, influencer: Influencer) -> List[Content]:
        pass

    @abstractmethod
    def delete_content(self, content_ids: List[str]):
        pass

    @abstractmethod
    def save_content(self, influencer: Influencer, content: List[Content]):
        pass