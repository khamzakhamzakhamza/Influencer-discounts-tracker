from datetime import datetime, timezone
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink

class AffiliatedLinkBuilder:
    def __init__(self):
        self.id = "57ae1dd2-592c-49f4-8f92-55a29a744ba2"
        self.prompt = "Moist Charlie Clips"
        self.tokens = ["moist", "charlie", "clips"]
        self.link = "sdfsadfsadf"
        self.creation_date = datetime.now(timezone.utc)
        self.version = 1

    def with_id(self, id: str):
        self.id = id
        return self
    
    def with_prompt(self, prompt: str):
        self.prompt = prompt
        return self
    
    def with_tokens(self, tokens: list[str]):
        self.tokens = tokens
        return self
    
    def with_link(self, link: str):
        self.link = link
        return self
    
    def with_creation_date(self, creation_date: datetime):
        self.creation_date = creation_date
        return self
    
    def with_version(self, version: int):
        self.version = version
        return self
    
    def build(self):
        return AffiliatedLink(self.id, self.prompt, self.tokens, self.link, self.creation_date, self.version)