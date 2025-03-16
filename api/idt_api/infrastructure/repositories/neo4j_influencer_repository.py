from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User
from typing import List, Optional
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_api.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jInfluencerRepository(InfluencerRepositoryInterface):    
    async def get_influencer_by_channel_id(self, channel_id: str) -> Optional[Influencer]:
        query = """
            MATCH (i:Influencer {channelId: $channel_id}) 
            RETURN i
        """
        
        influencer = None
        
        async with Neo4jSessionFactory() as session:
            result = await session.run(query, channel_id=channel_id)
        
            async for record in result:
                influencer = self.map_influencer(record)
            
        return influencer
    
    async def get_influencer_by_id(self, influencer_id: str) -> Optional[Influencer]:
        query = """
            MATCH (i:Influencer {id: $influencer_id}) 
            RETURN i
        """
        
        influencer = None
        
        async with Neo4jSessionFactory() as session:
            result = await session.run(query, influencer_id=influencer_id)
        
            async for record in result:
                influencer = self.map_influencer(record)
            
        return influencer
    
    async def create_influencer(self, influencer: Influencer, user: User) -> None:
        query = """
            MERGE (u:User {id: $user_id})
            CREATE (i:Influencer {
                id: $id,
                channelId: $channel_id,
                username: $username,
                title: $title,
                channelUrl: $channel_url,
                imageUrl: $image_url
            })
            MERGE (u)-[:FOLLOWS]->(i)
        """

        async with Neo4jSessionFactory() as session:
            await session.run(
                query,
                user_id=user.id,
                id=influencer.id,
                channel_id=influencer.channelId,
                username=influencer.username,
                title=influencer.title,
                channel_url=influencer.channelUrl,
                image_url=influencer.imageUrl
            )

    async def associate_user(self, influencer: Influencer, user: User) -> None:
        query = """
            MATCH (u:User {id: $user_id}), (i:Influencer {id: $influencer_id}) 
            MERGE (u)-[:FOLLOWS]->(i) 
            RETURN u, i
        """

        async with Neo4jSessionFactory() as session:
            await session.run(query, user_id=user.id, influencer_id=influencer.id)

    async def get_user_influencers(self, user: User) -> List[Influencer]:
        query = """
            MATCH (u:User {id: $user_id})-[:FOLLOWS]->(i:Influencer) 
            RETURN i
        """

        influencers = []

        async with Neo4jSessionFactory() as session:
            result = await session.run(query, user_id=user.id)
         
            async for record in result:
                influencer = self.map_influencer(record)
                influencers.append(influencer)

        return influencers
    
    async def disassociate_user_influencer(self, user: User, influencer: Influencer) -> int:
        query = """
            MATCH (u:User {id: $user_id})-[f:FOLLOWS]->(i:Influencer {id: $influencer_id}) 
            WITH f, COUNT(f) AS relCount
            DELETE f 
            RETURN relCount
        """

        async with Neo4jSessionFactory() as session:
            result = await session.run(query, user_id=user.id, influencer_id=influencer.id)
            async for record in result:
                return record['relCount']
        
        return 0
    
    def map_influencer(self, record) -> Influencer:
        return Influencer(record['i']['channelId'], record['i']['username'], record['i']['title'], record['i']['channelUrl'], record['i']['imageUrl'], record['i']['id'])
