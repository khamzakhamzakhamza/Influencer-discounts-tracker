from datetime import datetime, timedelta, timezone
from typing import List
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content
from tests.shared.builders.content_builder import ContentBuilder

class MockContentRepository(ContentRepositoryInterface):
    __content = [
        ContentBuilder().with_content_creation_date(datetime.now(timezone.utc) - timedelta(days=2)).build(),
        ContentBuilder().with_content_creation_date(datetime.now(timezone.utc) - timedelta(days=2)).build(),
        ContentBuilder().with_content_creation_date(datetime.now(timezone.utc) - timedelta(days=2)).build()
    ]

    def get_content(self, influencer: Influencer) -> List[Content]:
        return self.__content

    def delete_content(self, content_ids: List[str]):
        self.__content = [c for c in self.__content if c.id not in content_ids]
    
    def create_content(self, influencer: Influencer, content: List[Content]):
        self.__content.extend(content)
