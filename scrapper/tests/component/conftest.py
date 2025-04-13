import pytest
from idt_scrapper.domain.orchestrators.update_orchestrator import UpdateOrchestrator
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.domain.services.promo_service import PromoService
from tests.component.mock_repositories.mock_affiliated_link_repository import MockAffiliatedLinkRepository
from tests.component.mock_scanners.mock_affiliated_link_repository import MockAffiliatedLinkScanner
from tests.component.mock_scanners.mock_content_scanner import MockContentScanner
from tests.component.mock_repositories.mock_content_repository import MockContentRepository
from tests.component.mock_scanners.mock_influencer_scanner import MockInfluencerScanner
from tests.component.mock_repositories.mock_influencer_repository import MockInfluencerRepository

@pytest.fixture
def scrapper_fixture():
    influencer_repository = MockInfluencerRepository()
    influencer_scanner = MockInfluencerScanner()
    influencer_service = InfluencerService(influencer_repository, influencer_scanner)

    content_repository = MockContentRepository()
    content_scanner = MockContentScanner()
    content_service = ContentService(content_repository, content_scanner)

    affiliated_link_repository = MockAffiliatedLinkRepository()
    affiliated_link_scanner = MockAffiliatedLinkScanner()
    promo_service = PromoService(affiliated_link_repository, affiliated_link_scanner)

    return UpdateOrchestrator(influencer_service, content_service, promo_service)
