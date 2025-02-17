from neo4j import GraphDatabase

from idt_api.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

queries = [
    "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.username IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE"
]

def setup_db():
    with Neo4jSessionFactory() as session:
        for query in queries:
            session.run(query)
