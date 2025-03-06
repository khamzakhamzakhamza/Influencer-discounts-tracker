from typing import Optional
from uuid import uuid4

class Influencer:
    def __init__(self, channel_id: str, username: str, title: str, channelUrl: str, imageUrl: str, id: Optional[str] = None):
        self.id = id or str(uuid4())
        self.channelId = channel_id
        self.username = username
        self.title = title
        self.channelUrl = channelUrl
        self.imageUrl = imageUrl

    def __repr__(self):
        return f"User(id={self.id}, channelId={self.channelId}, username={self.username}, title={self.title}, channelUrl={self.channelUrl}, imageUrl={self.imageUrl})"
