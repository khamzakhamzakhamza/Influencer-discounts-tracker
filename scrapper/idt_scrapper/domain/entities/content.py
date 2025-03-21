from datetime import datetime

class Content:
    def __init__(self, id: str, prompt: str, content_url: str, creation_date: datetime, content_creation_date: datetime):
        self.id = id
        self.prompt = prompt
        self.content_url = content_url
        self.creation_date = creation_date
        self.content_creation_date = content_creation_date
        self.version = 1

    def __repr__(self):
        return f"Content(id={self.id}, prompt={self.prompt}, content_url={self.content_url}, creation_date={self.creation_date}, content_creation_date={self.content_creation_date}, version={self.version})"
