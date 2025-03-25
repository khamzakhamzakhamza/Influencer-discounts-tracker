from typing import List
from idt_scrapper.domain.scanners.promo_scanner_interface import PromoScannerInterface
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.entities.promo import Promo

class PromoScanner(PromoScannerInterface):
    def scan_promos(self, content: List[Content]) -> List[Promo]:
        pass
