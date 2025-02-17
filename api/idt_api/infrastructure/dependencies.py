from idt_api.infrastructure.repositories.neo4j_user_repository import Neo4jUserRepository

def get_user_repository():
    return Neo4jUserRepository()