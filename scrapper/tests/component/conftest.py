import pytest
from idt_scrapper.domain.orchestrators.update_orchestrator import UpdateOrchestrator
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.domain.services.promo_service import PromoService
from idt_scrapper.infrastructure.repositories.neo4j_affiliated_link_repository_interface import Neo4jAffiliatedLinkRepository
from idt_scrapper.infrastructure.scanners.beautiful_soup_affiliated_link_scanner import BeautifulSoupAffiliatedLinkScanner
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

    promo_repository = Neo4jAffiliatedLinkRepository()
    promo_scanner = BeautifulSoupAffiliatedLinkScanner()
    promo_service = PromoService(promo_repository, promo_scanner)

    return UpdateOrchestrator(influencer_service, content_service, promo_service)
