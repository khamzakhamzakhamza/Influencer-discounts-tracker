from typing import List
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content

class MockContentRepository(ContentRepositoryInterface):
    __content = [
        Content(
            '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            'The Best Content Ever',
            'The best content ever created',
            'https://www.youtube.com/watch?v=57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            '2021-09-20T19:00:00Z',
            '2021-09-20T19:00:00Z'),
        Content(
            '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            'The Best Content Ever',
            'The best content ever created',
            'https://www.youtube.com/watch?v=57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            '2021-09-20T19:00:00Z',
            '2021-09-20T19:00:00Z'),
        Content(
            '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            'The Best Content Ever',
            'The best content ever created',
            'https://www.youtube.com/watch?v=57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            '2021-09-20T19:00:00Z',
            '2021-09-20T19:00:00Z'),
    ]

    def get_content(self, influencer: Influencer) -> List[Content]:
        return self.__content

    def delete_content(self, content_ids: List[str]):
        self.__content = [c for c in self.__content if c.id not in content_ids]
    
    def create_content(self, influencer: Influencer, content: List[Content]):
        self.__content.extend(content)
