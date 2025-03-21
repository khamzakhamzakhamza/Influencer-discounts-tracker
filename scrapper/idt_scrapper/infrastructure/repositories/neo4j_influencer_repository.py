from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jInfluencerRepository(InfluencerRepositoryInterface):    
    def get_influencers_by_desc_update_date(self, count: int = 100) -> List[Influencer]:
        query = """
            MATCH (i:Influencer)
            RETURN i
            ORDER BY i.lastUpdateDate DESC
            LIMIT $count
        """
        
        influencers = []
        
        with Neo4jSessionFactory() as session:
            result = session.run(query, count=count)
        
            for record in result:
                influencers.append(self.map_influencer(record))
            
        return influencers
    
    def update_influencer(self, influencer: Influencer):
        query = """
            MERGE (i:Influencer {id: $id})
            ON MATCH SET 
                i.title = $title,
                i.imageUrl = $image_url
        """
        
        with Neo4jSessionFactory() as session:
            session.run(query, id=influencer.id, title=influencer.title, image_url=influencer.image_url)
    
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
