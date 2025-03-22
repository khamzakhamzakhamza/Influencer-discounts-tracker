import inject
from inject import Binder
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService

def domain_di_config(binder: Binder):
    binder.bind_to_provider(ContentService, lambda: ContentService(inject.instance(ContentRepositoryInterface), inject.instance(ContentScannerInterface)))
    binder.bind_to_provider(InfluencerService, lambda: InfluencerService(inject.instance(InfluencerRepositoryInterface), inject.instance(InfluencerScannerInterface)))
