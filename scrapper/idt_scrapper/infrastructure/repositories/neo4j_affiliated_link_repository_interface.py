from typing import List
from idt_scrapper.domain.repositories.affiliated_link_repository_interface import AffiliatedLinkRepositoryInterface
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.entities.promo import Promo

class Neo4jAffiliatedLinkRepository(AffiliatedLinkRepositoryInterface):
    def save_links(self, links: List[AffiliatedLink]) -> List[Promo]:
        pass