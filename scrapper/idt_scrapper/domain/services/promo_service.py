from typing import List
from idt_scrapper.domain.entities.promo import Promo
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.repositories.promo_repository_interface import PromoRepositoryInterface
from idt_scrapper.domain.scanners.promo_scanner_interface import PromoScannerInterface

class PromoService:
    def __init__(self, promo_repository: PromoRepositoryInterface, promo_scanner: PromoScannerInterface):
        self.promo_repository = promo_repository
        self.promo_scanner = promo_scanner

    def extract_promos(self, content: List[Content]) -> List[Promo]:
        promos = self.promo_scanner.scan_promos(content)
        return self.promo_repository.save_promos(promos)
