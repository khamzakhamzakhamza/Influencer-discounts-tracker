import requests
from typing import List
from urllib.parse import urlencode
from datetime import datetime, timedelta, timezone
from idt_scrapper.config import settings
from idt_scrapper.domain.entities.promocode import Promocode
from idt_scrapper.domain.scanners.promocode_scanner_intrerface import PromocodeScannerInterface
from idt_scrapper.domain.errors.scanning_error import ScanningError

class YouTubePromocodeScanner(PromocodeScannerInterface):
    def scan_promocodes(self, channel_id: str) -> List[Promocode]:
        base_url = "https://www.googleapis.com/youtube/v3/channels"
        query_params = {
            "part": "contentDetails",
            "id": channel_id,
            "key": settings.YOUTUBE_API_KEY
        }
        url = f"{base_url}?{urlencode(query_params)}"
        
        response = requests.get(url).json()
        uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
        query_params = {
            "part": "snippet",
            "playlistId": uploads_playlist_id,
            "maxResults": 50,
            "key": settings.YOUTUBE_API_KEY
        }
        url = f"{base_url}?{urlencode(query_params)}"
        
        response = requests.get(url).json()
        one_year_ago = (datetime.now(timezone.utc) - timedelta(days=365)).isoformat() + "Z"
        video_ids = [
            item["snippet"]["resourceId"]["videoId"]
            for item in response["items"]
            if item["snippet"]["publishedAt"] > one_year_ago
        ]

        video_id_string = ",".join(video_ids)

        base_url = "https://www.googleapis.com/youtube/v3/videos"
        query_params = {
            "part": "snippet",
            "id": video_id_string,
            "key": settings.YOUTUBE_API_KEY
        }
        url = f"{base_url}?{urlencode(query_params)}"
        response = requests.get(url).json()

        pass

    def build_promocode(self, snippet: any) -> Promocode:
        pass
