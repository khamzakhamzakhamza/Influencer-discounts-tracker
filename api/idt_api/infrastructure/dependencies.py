from idt_api.infrastructure.repositories.neo4j_influencer_repository import Neo4jInfluencerRepository
from idt_api.infrastructure.repositories.neo4j_user_repository import Neo4jUserRepository
from idt_api.infrastructure.scanners.youtube_influencer_scanner import YouTubeInfluencerScanner

def get_user_repository():
    return Neo4jUserRepository()

def get_influencer_repository():
    return Neo4jInfluencerRepository()

def get_influencer_scanner():
    return YouTubeInfluencerScanner()