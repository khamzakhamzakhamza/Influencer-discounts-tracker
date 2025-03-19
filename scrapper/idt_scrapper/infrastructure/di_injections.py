from inject import Binder
from scrapper.idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from scrapper.idt_scrapper.domain.repositories.promocode_repository_interface import PromocodeRepositoryInterface
from scrapper.idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from scrapper.idt_scrapper.domain.scanners.promocode_scanner_intrerface import PromocodeScannerInterface
from scrapper.idt_scrapper.infrastructure.repositories.neo4j_influencer_repository import Neo4jInfluencerRepository
from scrapper.idt_scrapper.infrastructure.repositories.neo4j_promocode_repository import Neo4jPromocodeRepository
from scrapper.idt_scrapper.infrastructure.scanners.youtube_influencer_scanner import YouTubeInfluencerScanner
from scrapper.idt_scrapper.infrastructure.scanners.youtube_promocode_scanner import YouTubePromocodeScanner

def di_config(binder: Binder):
    binder.bind(PromocodeScannerInterface, YouTubePromocodeScanner())
    binder.bind(InfluencerScannerInterface, YouTubeInfluencerScanner())
    binder.bind(PromocodeRepositoryInterface, Neo4jPromocodeRepository())
    binder.bind(InfluencerRepositoryInterface, Neo4jInfluencerRepository())
