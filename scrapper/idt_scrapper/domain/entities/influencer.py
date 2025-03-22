from datetime import datetime

class Influencer:
    def __init__(self, channel_id: str, username: str, title: str, channel_url: str, image_url: str, id: str, last_update_date: datetime, creation_date: datetime):
        self.id = id
        self.channel_id = channel_id
        self.username = username
        self.title = title
        self.channel_url = channel_url
        self.image_url = image_url
        self.last_update_date = last_update_date
        self.creation_date = creation_date
        self.version = 1

    def __repr__(self):
        return f"Influencer(id={self.id}, channel_id={self.channel_id}, username={self.username}, title={self.title}, channel_url={self.channel_url}, image_url={self.image_url}, update_time={self.last_update_date}, created_time={self.creation_date}, version={self.version})"
