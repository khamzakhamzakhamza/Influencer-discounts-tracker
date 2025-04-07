from typing import List
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.repositories.affiliated_link_repository_interface import AffiliatedLinkRepositoryInterface
from idt_scrapper.domain.scanners.affiliated_link_scanner_interface import AffiliatedLinkScannerInterface
from idt_scrapper.domain.entities.promo import Promo

class PromoService:
    def __init__(self, affiliated_link_repository: AffiliatedLinkRepositoryInterface, affiliated_link_scanner: AffiliatedLinkScannerInterface):
        self.affiliated_link_repository = affiliated_link_repository
        self.affiliated_link_scanner = affiliated_link_scanner

    def extract_promos(self, content: List[Content]):
        for _content in content:
            links = self.affiliated_link_scanner.scan_links(_content)
            self.affiliated_link_repository.save_links(_content, links)
