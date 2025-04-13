from typing import List
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.scanners.affiliated_link_scanner_interface import AffiliatedLinkScannerInterface
from idt_scrapper.domain.entities.content import Content
from tests.shared.builders.affiliated_link_builder import AffiliatedLinkBuilder

class MockAffiliatedLinkScanner(AffiliatedLinkScannerInterface):
    def scan_links(self, content: Content) -> List[AffiliatedLink]:
        return [
            AffiliatedLinkBuilder().with_link("https://example.com").build(),
        ]
