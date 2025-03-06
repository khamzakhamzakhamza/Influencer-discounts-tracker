from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User
from typing import List, Optional
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_api.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jInfluencerRepository(InfluencerRepositoryInterface):    
    async def get_influencer(self, chennel_id: str) -> Optional[Influencer]:
        query = f"MATCH (i:Influencer) WHERE i.channelId = '{chennel_id}' RETURN i"
        
        influencer = None
        
        async with Neo4jSessionFactory() as session:
            result = await session.run(query)
        
            async for record in result:
                influencer = Influencer(record['i']['channelId'], record['i']['username'], record['i']['title'], record['i']['channelUrl'], record['i']['imageUrl'], record['i']['id'])
            
        return influencer
    
    async def create_influencer(self, influencer: Influencer) -> None:
        query = f"CREATE (i:Influencer {{id: '{influencer.id}', channelId: '{influencer.channelId}', username: '{influencer.username}', title: '{influencer.title}', channelUrl: '{influencer.channelUrl}', imageUrl: '{influencer.imageUrl}'}})"

        async with Neo4jSessionFactory() as session:
            await session.run(query)
    
    async def associate_user(self, influencer: Influencer, user: User) -> None:
        query = f"MATCH (u:User {{id: '{user.id}'}}), (i:Influencer {{id: '{influencer.id}'}}) MERGE (u)-[:FOLLOWS]->(i) RETURN u, i;"
        
        async with Neo4jSessionFactory() as session:
            await session.run(query)

    async def get_user_influencers(self, user: User) -> List[Influencer]:
        query = f"MATCH (u:User {{id: '{user.id}'}})-[:FOLLOWS]->(i:Influencer) RETURN i"

        influencers = []
       
        async with Neo4jSessionFactory() as session:
            result = await session.run(query)
         
            async for record in result:
                influencer = Influencer(record['i']['channelId'], record['i']['username'], record['i']['title'], record['i']['channelUrl'], record['i']['imageUrl'], record['i']['id'])
                influencers.append(influencer)

        return influencers