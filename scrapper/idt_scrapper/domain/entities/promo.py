from abc import ABC
from datetime import datetime
from typing import List

class Promo(ABC):
    def __init__(self, id: str, prompt: str, tokens: List[str], creation_date: datetime, version: int):
        self.id = id
        self.prompt = prompt
        self.tokens = tokens
        self.creation_date = creation_date
        self.version = version

    def __repr__(self):
        return f"Promo(id={self.id}, prompt={self.prompt}, tokens={self.tokens}, creation_date={self.creation_date}, version={self.version})"