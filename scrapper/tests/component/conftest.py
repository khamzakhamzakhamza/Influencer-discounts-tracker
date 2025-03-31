import pytest
from idt_scrapper.domain.orchestrators.update_orchestrator import UpdateOrchestrator
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.domain.services.promo_service import PromoService
from idt_scrapper.infrastructure.repositories.neo4j_promo_repository import Neo4jPromoRepository
from idt_scrapper.infrastructure.scanners.promo_scanner import PromoScanner
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

    promo_repository = Neo4jPromoRepository()
    promo_scanner = PromoScanner()
    promo_service = PromoService(promo_repository, promo_scanner)

    return UpdateOrchestrator(influencer_service, content_service, promo_service)
