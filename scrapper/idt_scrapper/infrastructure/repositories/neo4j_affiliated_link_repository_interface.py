from typing import List
from idt_scrapper.domain.repositories.affiliated_link_repository_interface import AffiliatedLinkRepositoryInterface
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jAffiliatedLinkRepository(AffiliatedLinkRepositoryInterface):
    def save_links(self, content: Content, links: List[AffiliatedLink]):
        query = """
            MERGE (c:Content {id: $content_id})
            WITH c, $links AS links
            UNWIND links AS link
            CREATE (l:AffiliatedLink {
                id: link.id,
                prompt: link.prompt,
                tokens: link.tokens,
                link: link.link,
                creationDate: link.creationDate,
                version: link.version
            })
            MERGE (c)-[:HAS_AFFILIATED_LINK]->(l)
        """

        links_data = [
            {
                "id": l.id,
                "prompt": l.prompt,
                "tokens": l.tokens,
                "link": l.link,
                "creationDate": l.creation_date,
                "version": l.version,
            }
            for l in links
        ]

        with Neo4jSessionFactory() as session:
            session.run(query, content_id=content.id, links=links_data)
