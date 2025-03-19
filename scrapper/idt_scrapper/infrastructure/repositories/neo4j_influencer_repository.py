from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jInfluencerRepository(InfluencerRepositoryInterface):    
    def get_influencers_by_desc_update_date(self, count: int = 100) -> List[Influencer]:
        pass
    
    def update_influencer(self, influencer: Influencer):
        pass
    
    def map_influencer(self, record) -> Influencer:
        return Influencer(
            record['i']['channelId'],
            record['i']['username'],
            record['i']['title'],
            record['i']['channelUrl'],
            record['i']['imageUrl'],
            record['i']['id'],
            record['i']['lastUpdateDate'],
            record['i']['creationDate'])
