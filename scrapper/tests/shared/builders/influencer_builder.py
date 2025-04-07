from datetime import datetime, timezone
from idt_scrapper.domain.entities.influencer import Influencer

class InfluencerBuilder:
    def __init__(self):
        self.id = "57ae1dd2-592c-49f4-8f92-55a29a744ba2"
        self.channel_id ="UC4EQHfzIbkL_Skit_iKt1aA"
        self.username =  "@moistcharlieclipsofficial"
        self.title = "Moist Charlie Clips"
        self.channel_url = "https://www.youtube.com/@moistcharlieclipsofficial"
        self.image_url = "https://yt3.ggpht.com/uNnYRnCNiXwSx3IZcJoV0fRmDlTQIsIu4rHsGWvLSjGslrv-D4m1bUO6c7-0zoU4J8ol-9OrNvo=s88-c-k-c0x00ffffff-no-rj"
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