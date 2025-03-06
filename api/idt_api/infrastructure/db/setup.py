from neo4j import GraphDatabase

from idt_api.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

queries = [
    "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.username IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (i:Influencer) REQUIRE i.channelId IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (i:Influencer) REQUIRE i.id IS UNIQUE"
]

async def setup_db():
    async with Neo4jSessionFactory() as session:
        for query in queries:
            await session.run(query)
