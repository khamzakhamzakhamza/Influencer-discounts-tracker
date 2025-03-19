from neo4j import AsyncGraphDatabase, Session
# from idt_api.api.config.settings import settings

class Neo4jSessionFactory:
    def __init__(self):
        self._driver = AsyncGraphDatabase.driver(settings.DB_URL, auth=(settings.DB_USERNAME, settings.DB_PASSWORD))

    async def __aenter__(self) -> Session:
        return self._driver.session()

    async def __aexit__(self, *_):
        await self._driver.close()
