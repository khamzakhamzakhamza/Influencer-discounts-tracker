from datetime import datetime, timezone
from idt_scrapper.domain.entities.influencer import Influencer

class InfluencerBuilder:
    def __init__(self):
        self.id = "id"
        self.channel_id = "channel_id"
        self.username = "username"
        self.title = "title"
        self.channel_url = "channel_url"
        self.image_url = "image_url"
        self.last_update_date = datetime.now(timezone.utc)
        self.creation_date = datetime.now(timezone.utc)
        self.version = 1

    def with_id(self, id: str):
        self.id = id
        return self
    
    def with_channel_id(self, channel_id: str):
        self.channel_id = channel_id
        return self
    
    def with_username(self, username: str):
        self.username = username
        return self
    
    def with_title(self, title: str):
        self.title = title
        return self
    
    def with_channel_url(self, channel_url: str):
        self.channel_url = channel_url
        return self
    
    def with_image_url(self, image_url: str):
        self.image_url = image_url
        return self
    
    def with_last_update_date(self, last_update_date: datetime):
        self.last_update_date = last_update_date
        return self
    
    def with_creation_date(self, creation_date: datetime):
        self.creation_date = creation_date
        return self
    
    def with_version(self, version: int):
        self.version = version
        return self
    
    def build(self):
        return Influencer(self.id, self.channel_id, self.username, self.title, self.channel_url, self.image_url, self.last_update_date, self.creation_date, self.version)