from typing import List
from scrapper.idt_scrapper.domain.entities.promocode import Promocode
from scrapper.idt_scrapper.domain.repositories.promocode_repository_interface import PromocodeRepositoryInterface
from scrapper.idt_scrapper.infrastructure.db.neo4j_session_factory import Neo4jSessionFactory

class Neo4jPromocodeRepository(PromocodeRepositoryInterface):
    def delete_promocodes(self, promocode_ids: List[str]):
        pass
    
    def create_promocodes(self, promocodes: List[Promocode]):
        pass
    
    def map_promocode(self, record) -> Promocode:
        return Promocode(
            record['i']['id'],
            record['i']['code'],
            record['i']['prompt'],
            record['i']['shopUrl'],
            record['i']['contentUrl'],
            record['i']['discountValue'],
            record['i']['creationDate'],
            record['i']['expirationDate'],
            record['i']['startDate'])
