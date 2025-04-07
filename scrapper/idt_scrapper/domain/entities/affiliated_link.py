from datetime import datetime
from typing import List
from idt_scrapper.domain.entities.promo import Promo

class AffiliatedLink(Promo):
    def __init__(self, id: str, prompt: str, tokens: List[str], link: str, creation_date: datetime, version: int = 1):
        super().__init__(id, prompt, tokens, creation_date, version)
        self.link = link

    def __repr__(self):
        return f"AffiliatedLink(id={self.id}, prompt={self.prompt}, tokens={self.tokens}, link={self.link}, creation_date={self.creation_date}, version={self.version})"
