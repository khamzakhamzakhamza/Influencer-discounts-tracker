from idt_api.domain.entities.user import User
from typing import Optional
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface
from idt_api.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jUserRepository(UserRepositoryInterface):
    async def create_user(self, user: User) -> None:
        query = """
            CREATE (u:User {
                id: $id,
                username: $username
            })
        """

        async with Neo4jSessionFactory() as session:
            await session.run(query, id=user.id, username=user.username)

    async def get_user(self, username: str) -> Optional[User]:
        query = """
            MATCH (u:User {username: $username})
            RETURN u
        """
        
        user = None
        
        async with Neo4jSessionFactory() as session:
            result = await session.run(query, username=username)
        
            async for record in result:
                user = User(record['u']['username'], record['u']['id'])
            
        return user
