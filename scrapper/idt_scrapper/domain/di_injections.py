import inject
from inject import Binder
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.domain.services.promo_service import PromoService
from idt_scrapper.domain.repositories.affiliated_link_repository_interface import AffiliatedLinkRepositoryInterface
from idt_scrapper.domain.scanners.affiliated_link_scanner_interface import AffiliatedLinkScannerInterface

def domain_di_config(binder: Binder):
    binder.bind_to_provider(ContentService, lambda: ContentService(inject.instance(ContentRepositoryInterface), inject.instance(ContentScannerInterface)))
    binder.bind_to_provider(InfluencerService, lambda: InfluencerService(inject.instance(InfluencerRepositoryInterface), inject.instance(InfluencerScannerInterface)))
    binder.bind_to_provider(PromoService, lambda: PromoService(inject.instance(AffiliatedLinkRepositoryInterface), inject.instance(AffiliatedLinkScannerInterface)))
