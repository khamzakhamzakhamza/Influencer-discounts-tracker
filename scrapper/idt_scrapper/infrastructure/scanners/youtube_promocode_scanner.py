from typing import List
import requests
from scrapper.idt_scrapper.domain.entities.promocode import Promocode
from scrapper.idt_scrapper.domain.scanners.promocode_scanner_intrerface import PromocodeScannerInterface

class YouTubePromocodeScanner(PromocodeScannerInterface):
    def scan_promocodes(self, channel_id: str) -> List[Promocode]:
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={influencer.channel_id}&key={settings.YOUTUBE_API_KEY}"

        response = requests.get(url)

        # TODO: handle faulty response from youtube api

        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            self.build_influencer(influencer, data["items"][0]["snippet"])
                
        # TODO: throw error if not found 

    def build_promocode(self, snippet: any) -> Promocode:
        pass
