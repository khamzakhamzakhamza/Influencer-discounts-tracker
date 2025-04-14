from typing import List
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content

class Neo4jContentRepository(ContentRepositoryInterface):
    def get_content(self, influencer: Influencer) -> List[Content]:
        query = """
            MATCH (i:Influencer {id: $influencer_id})-[:HAS_CONTENT]->(c:Content) 
            RETURN c
            ORDER BY c.contentCreationDate DESC
        """

        with Neo4jSessionFactory() as session:
            result = session.run(query, influencer_id=influencer.id)
            return [self.map_content(record) for record in result]

    def delete_content(self, content_ids: List[str]):
        query = """
            MATCH (c:Content)
            WHERE c.id IN $ids
            OPTIONAL MATCH (c)-[:HAS_PROMO]->(ref)
            DETACH DELETE c, ref
        """
        with Neo4jSessionFactory() as session:
            session.run(query, ids=content_ids)
    
    def save_content(self, influencer: Influencer, content: List[Content]):
        query = """
            MERGE (i:Influencer {id: $influencer_id})
            WITH i, $contents AS contents
            UNWIND contents AS content
            CREATE (c:Content {
                id: content.id,
                title: content.title,
                prompt: content.prompt,
                contentUrl: content.contentUrl,
                creationDate: content.creationDate,
                contentCreationDate: content.contentCreationDate,
                version: content.version
            })
            MERGE (i)-[:HAS_CONTENT]->(c)
        """

        content_data = [
            {
                "id": c.id,
                "title": c.title,
                "prompt": c.prompt,
                "contentUrl": c.content_url,
                "creationDate": c.creation_date,
                "contentCreationDate": c.content_creation_date,
                "version": c.version,
            }
            for c in content
        ]

        with Neo4jSessionFactory() as session:
            session.run(query, influencer_id=influencer.id, contents=content_data)

    def map_content(self, record) -> Content:
        return Content(
            record['c']['id'],
            record['c']['title'],
            record['c']['prompt'],
            record['c']['contentUrl'],
            record['c']['creationDate'],
            record['c']['contentCreationDate'],
            record['c']['version'])
