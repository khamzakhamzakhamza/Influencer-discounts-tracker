from typing import List
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.repositories.affiliated_link_repository_interface import AffiliatedLinkRepositoryInterface
from idt_scrapper.domain.entities.content import Content
from tests.shared.builders.affiliated_link_builder import AffiliatedLinkBuilder

class MockAffiliatedLinkRepository(AffiliatedLinkRepositoryInterface):
    __links = [
        AffiliatedLinkBuilder().build(),
        AffiliatedLinkBuilder().build()
    ]

    def save_links(self, content: Content, links: List[AffiliatedLink]):
        self.__links.extend(links)
