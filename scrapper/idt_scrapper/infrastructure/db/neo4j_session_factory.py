from neo4j import GraphDatabase, Session
from idt_scrapper.config import settings

class Neo4jSessionFactory:
    def __init__(self):
        self._driver = GraphDatabase.driver(settings.DB_URL, auth=(settings.DB_USERNAME, settings.DB_PASSWORD))

    def __enter__(self) -> Session:
        return self._driver.session()

    def __exit__(self, *_):
        self._driver.close()
