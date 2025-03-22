from datetime import datetime

class Content:
    def __init__(self, id: str, title: str, prompt: str, content_url: str, creation_date: datetime, content_creation_date: datetime, version: int = 1):
        self.id = id
        self.title = title
        self.prompt = prompt
        self.content_url = content_url
        self.creation_date = creation_date
        self.content_creation_date = content_creation_date
        self.version = version

    def __repr__(self):
        return f"Content(id={self.id}, title={self.title}, prompt={self.prompt}, content_url={self.content_url}, creation_date={self.creation_date}, content_creation_date={self.content_creation_date}, version={self.version})"
