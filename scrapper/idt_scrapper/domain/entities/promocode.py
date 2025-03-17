from datetime import datetime
from typing import Optional

class Promocode:
    def __init__(self, id: str, code: Optional[str], prompt: str, shop_url: str, content_url: str, discount_value: int, creation_date: datetime, expiration_date: datetime, start_date: datetime):
        self.id = id
        self.code = code
        self.prompt = prompt
        self.shop_url = shop_url
        self.content_url = content_url
        self.discount_value = discount_value
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.start_date = start_date
        self.version = 1

    def __repr__(self):
        return f"Promocode(id={self.id}, code={self.code}, prompt={self.prompt}, shop_url={self.shop_url}, content_url={self.content_url}, discount_value={self.discount_value}, creation_date={self.creation_date}, expiration_date={self.expiration_date}, start_date={self.start_date}, version={self.version})"
