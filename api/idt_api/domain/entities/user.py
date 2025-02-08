from typing import Optional
from uuid import uuid4

class User:
    def __init__(self, username: str, id: Optional[str] = None):
        self.id = id or str(uuid4())
        self.username = username

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"
