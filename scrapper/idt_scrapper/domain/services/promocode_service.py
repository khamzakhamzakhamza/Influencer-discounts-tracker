from typing import List
from datetime import datetime
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.promocode import Promocode
from idt_scrapper.domain.repositories.promocode_repository_interface import PromocodeRepositoryInterface
from idt_scrapper.domain.scanners.promocode_scanner_intrerface import PromocodeScannerInterface

class PromocodeService:
    def __init__(self, promocode_repository: PromocodeRepositoryInterface, promocode_scanner: PromocodeScannerInterface):
        self._promocode_repository = promocode_repository
        self._promocode_scanner = promocode_scanner
    
    def delete_stale(self, influencer: Influencer):
        promocodes = self._promocode_repository.get_promocodes(influencer)
        promocodes_to_delete = []

        for promocode in promocodes:
            current_time = datetime.now(datetime.timezone.utc)
            if promocode.expiration_date <= current_time:
                promocodes_to_delete.append(promocode.id)

        self._promocode_repository.delete_promocodes(promocodes_to_delete)

    def save_promocodes(self, influencer: Influencer) -> List[Promocode]:
        promocodes = self._promocode_scanner.scan_content(influencer)
        self._promocode_repository.create_promocodes(promocodes)
        return promocodes