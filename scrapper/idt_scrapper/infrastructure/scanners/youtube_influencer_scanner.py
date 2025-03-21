import requests
from urllib.parse import urlencode
from idt_scrapper.config import settings
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.errors.scanning_error import ScanningError

class YouTubeInfluencerScanner(InfluencerScannerInterface):
    def rescan_influencer(self, influencer: Influencer):
        base_url = "https://www.googleapis.com/youtube/v3/channels"
        query_params = {
            "part": "snippet",
            "id": influencer.channel_id,
            "key": settings.YOUTUBE_API_KEY
        }
        url = f"{base_url}?{urlencode(query_params)}"

        response = requests.get(url)
        if not response.ok:
            raise ScanningError(influencer, "rescan_influencer")

        data = response.json()
        if "items" not in data or len(data["items"]) == 0:
            raise ScanningError(influencer, "rescan_influencer")

        self.update_influencer(influencer, data["items"][0]["snippet"])

    def update_influencer(self, influencer: Influencer, snippet: any) -> Influencer:
        influencer.image_url = snippet["thumbnails"]["default"]["url"]
        influencer.title = snippet["title"]
