import inject
from inject import Binder
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.repositories.promocode_repository_interface import PromocodeRepositoryInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.scanners.promocode_scanner_intrerface import PromocodeScannerInterface
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.promocode_service import PromocodeService

def domain_di_config(binder: Binder):
    binder.bind(PromocodeService, lambda: PromocodeService(inject.instance(PromocodeRepositoryInterface), inject.instance(PromocodeScannerInterface)))
    binder.bind(InfluencerService, lambda: InfluencerService(inject.instance(InfluencerRepositoryInterface), inject.instance(InfluencerScannerInterface)))
