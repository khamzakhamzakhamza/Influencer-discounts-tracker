from datetime import datetime
from typing import List, Optional

class Promo:
    def __init__(self, id: str, code: Optional[str], tokens: str, tags: List[str], link: str, discount_value: Optional[int], creation_date: datetime, version: int = 1):
        self.id = id
        self.code = code
        self.tokens = tokens
        self.link = link
        self.tags = tags
        self.discount_value = discount_value
        self.creation_date = creation_date
        self.version = version

    def __repr__(self):
        return f"Promo(id={self.id}, code={self.code}, tokens={self.tokens}, tags={self.tags}, link={self.link}, discount_value={self.discount_value}, creation_date={self.creation_date}, version={self.version})"
