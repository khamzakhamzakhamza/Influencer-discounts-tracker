from datetime import datetime, timezone
from idt_scrapper.domain.entities.content import Content

class ContentBuilder:
    def __init__(self):
        self.id = "id"
        self.title = "title"
        self.prompt = "prompt"
        self.content_url = "content_url"
        self.creation_date = datetime.now(timezone.utc)
        self.content_creation_date = datetime.now(timezone.utc)
        self.version = 1

    def with_id(self, id: str):
        self.id = id
        return self
    
    def with_title(self, title: str):
        self.title = title
        return self
    
    def with_prompt(self, prompt: str):
        self.prompt = prompt
        return self
    
    def with_content_url(self, content_url: str):
        self.content_url = content_url
        return self
    
    def with_creation_date(self, creation_date: datetime):
        self.creation_date = creation_date
        return self
    
    def with_content_creation_date(self, content_creation_date: datetime):
        self.content_creation_date = content_creation_date
        return self
    
    def with_version(self, version: int):
        self.version = version
        return self
    
    def build(self):
        return Content(self.id, self.title, self.prompt, self.content_url, self.creation_date, self.content_creation_date, self.version)
