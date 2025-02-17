from neo4j import GraphDatabase, Session
from idt_api.api.config.settings import settings

class Neo4jSessionFactory:
    def __init__(self):
        self._driver = GraphDatabase.driver(settings.DB_URL, auth=(settings.DB_USERNAME, settings.DB_PASSWORD))

    def __enter__(self) -> Session:
        return self._driver.session()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._driver.close()
