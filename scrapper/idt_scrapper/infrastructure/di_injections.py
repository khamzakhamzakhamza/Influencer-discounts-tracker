from inject import Binder
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.infrastructure.repositories.neo4j_influencer_repository import Neo4jInfluencerRepository
from idt_scrapper.infrastructure.repositories.neo4j_content_repository import Neo4jContentRepository
from idt_scrapper.infrastructure.scanners.youtube_influencer_scanner import YouTubeInfluencerScanner
from idt_scrapper.infrastructure.scanners.youtube_content_scanner import YouTubeContentScanner
from idt_scrapper.domain.scanners.promo_scanner_interface import PromoScannerInterface
from idt_scrapper.infrastructure.scanners.promo_scanner import PromoScanner
from idt_scrapper.domain.repositories.promo_repository_interface import PromoRepositoryInterface
from idt_scrapper.infrastructure.repositories.neo4j_promo_repository import Neo4jPromoRepository

def infrastructure_di_config(binder: Binder):
    binder.bind(ContentScannerInterface, YouTubeContentScanner())
    binder.bind(InfluencerScannerInterface, YouTubeInfluencerScanner())
    binder.bind(ContentRepositoryInterface, Neo4jContentRepository())
    binder.bind(InfluencerRepositoryInterface, Neo4jInfluencerRepository())
    binder.bind(PromoScannerInterface, PromoScanner())
    binder.bind(PromoRepositoryInterface, Neo4jPromoRepository())
