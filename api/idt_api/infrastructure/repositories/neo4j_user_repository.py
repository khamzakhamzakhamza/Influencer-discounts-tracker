from idt_api.domain.entities.user import User
from typing import Optional
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface
from idt_api.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jUserRepository(UserRepositoryInterface):
    def create_user(self, user: User) -> None:
        query = f"CREATE (u:User {{username: '{user.username}', id: '{user.id}'}})"

        with Neo4jSessionFactory() as session:
            session.run(query)

    def get_user(self, username: str) -> Optional[User]:
        query = f"MATCH (u:User) WHERE u.username = '{username}' RETURN u"
        
        user = None
        
        with Neo4jSessionFactory() as session:
            result = session.run(query)
        
            for record in result:
                user = User(record['u']['username'], record['u']['id'])
            
        return user
