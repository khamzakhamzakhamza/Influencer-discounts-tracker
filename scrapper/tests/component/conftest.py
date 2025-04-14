from unittest.mock import MagicMock
import pytest
from idt_scrapper.domain.orchestrators.update_orchestrator import UpdateOrchestrator
from idt_scrapper.domain.repositories.affiliated_link_repository_interface import AffiliatedLinkRepositoryInterface
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.scanners.affiliated_link_scanner_interface import AffiliatedLinkScannerInterface
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.domain.services.promo_service import PromoService

@pytest.fixture
def scrapper_fixture():
    influencer_repository_mock = MagicMock(spec=InfluencerRepositoryInterface)
    influencer_scanner_mock = MagicMock(spec=InfluencerScannerInterface)
    influencer_service = InfluencerService(influencer_repository_mock, influencer_scanner_mock)

    content_repository_mock = MagicMock(ContentRepositoryInterface)
    content_scanner_mock = MagicMock(ContentScannerInterface)
    content_service = ContentService(content_repository_mock, content_scanner_mock)

    affiliated_link_repository_mock = MagicMock(AffiliatedLinkRepositoryInterface)
    affiliated_link_scanner_mock = MagicMock(AffiliatedLinkScannerInterface)
    promo_service = PromoService(affiliated_link_repository_mock, affiliated_link_scanner_mock)

    return (influencer_repository_mock, content_repository_mock, content_scanner_mock, affiliated_link_repository_mock, affiliated_link_scanner_mock, UpdateOrchestrator(influencer_service, content_service, promo_service))
