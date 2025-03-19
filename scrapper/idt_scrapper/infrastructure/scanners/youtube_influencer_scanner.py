import requests
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface

class YouTubeInfluencerScanner(InfluencerScannerInterface):
    def rescan_influencer(self, influencer: Influencer):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={influencer.channel_id}&key={settings.YOUTUBE_API_KEY}"

        response = requests.get(url)

        # TODO: handle faulty response from youtube api

        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            self.build_influencer(influencer, data["items"][0]["snippet"])
                
        # TODO: throw error if not found 

    def build_influencer(self, influencer: Influencer, snippet: any) -> Influencer:
        influencer.image_url = snippet["thumbnails"]["default"]["url"]
        influencer.title = snippet["title"]
