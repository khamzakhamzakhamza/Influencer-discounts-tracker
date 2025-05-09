import requests
from typing import List, Optional
from urllib.parse import urlencode
from datetime import datetime, timezone
from idt_scrapper.config import settings
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.errors.scanning_error import ScanningError
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.entities.content import Content

# TODO: test this shit
class YouTubeContentScanner(ContentScannerInterface):
    CONTENT_LIMIT = 1000
    YOUTUBE_SEARCH_MAX_RESULTS = 50

    def scan_content(self, influencer: Influencer, cutoff_date: datetime) -> List[Content]:
        uploads_playlist_id = self.get_playlist_id(influencer)
        video_ids = self.get_video_ids(uploads_playlist_id, cutoff_date)
        videos = self.get_videos(video_ids)

        content = [
            self.build_content(video)
            for video in videos
        ]

        return content

    def get_playlist_id(self, influencer: Influencer) -> str:
        base_url = "https://www.googleapis.com/youtube/v3/channels"
        query_params = {
            "part": "contentDetails",
            "id": influencer.channel_id,
            "key": settings.YOUTUBE_API_KEY
        }
        url = f"{base_url}?{urlencode(query_params)}"
        
        response = requests.get(url)
        if not response.ok:
            raise ScanningError(influencer, "get_playlist_id_fetch", Exception(response.text))
        
        try:
            data = response.json()
            playlist_id = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
            return playlist_id
        except Exception as e:
            raise ScanningError(influencer, "get_playlist_id_parse", e)

    def get_video_ids(self, playlist_id: str, cutoff_date: datetime) -> List[str]:
        cutoff_date = cutoff_date.isoformat() + "Z"

        video_ids = []
        fetch_more = True
        page_token = None
        while fetch_more and len(video_ids) < self.CONTENT_LIMIT:
            data = self.fetch_video_ids(playlist_id, page_token)
            
            for item in data["items"]:
                if item["snippet"]["publishedAt"] < cutoff_date:
                    fetch_more = False
                    break

                video_ids.append(item["snippet"]["resourceId"]["videoId"])
            
            if "nextPageToken" in data:
                page_token = data["nextPageToken"]
            else:
                fetch_more = False

        return video_ids
        
    def fetch_video_ids(self, playlist_id: str, page_token: Optional[str]) -> any:
        base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
        query_params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "maxResults": self.YOUTUBE_SEARCH_MAX_RESULTS,
            "key": settings.YOUTUBE_API_KEY
        }

        if page_token is not None:
            query_params["pageToken"] = page_token

        url = f"{base_url}?{urlencode(query_params)}"
        
        response = requests.get(url)
        if not response.ok:
            raise ScanningError(playlist_id, "get_video_ids_fetch", Exception(response.text))

        try:
            return response.json()
        except Exception as e:
            raise ScanningError(playlist_id, "get_video_ids_parse", e)

    def get_videos(self, video_ids: List[str]) -> List[any]:
        curr_id = 0
        videos = []

        while curr_id < len(video_ids):
            video_ids_slice = video_ids[curr_id:curr_id+self.YOUTUBE_SEARCH_MAX_RESULTS]
            videos_json = self.fetch_videos(video_ids_slice)
            videos += videos_json["items"]
            curr_id += self.YOUTUBE_SEARCH_MAX_RESULTS

        return videos

    def fetch_videos(self, video_ids: List[str]) -> any:
        video_id_string = ",".join(video_ids)

        base_url = "https://www.googleapis.com/youtube/v3/videos"
        query_params = {
            "part": "snippet",
            "id": video_id_string,
            "key": settings.YOUTUBE_API_KEY
        }
        url = f"{base_url}?{urlencode(query_params)}"

        response = requests.get(url)
        if not response.ok:
            raise ScanningError(video_id_string, "get_videos_fetch", Exception(response.text))

        try:
            return response.json()
        except Exception as e:
            raise ScanningError(video_id_string, "get_videos_fetch", e)
        
    def build_content(self, video: any) -> Content:
        return Content(
            id = video["id"],
            title = video["snippet"]["title"],
            prompt = video["snippet"]["description"],
            content_url = f"https://www.youtube.com/watch?v={video['id']}",
            creation_date=datetime.now(timezone.utc),
            content_creation_date = datetime.fromisoformat(video["snippet"]["publishedAt"].replace("Z", "+00:00"))
        )
