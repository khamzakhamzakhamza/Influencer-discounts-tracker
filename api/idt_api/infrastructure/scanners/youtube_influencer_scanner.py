from idt_api.api.config.settings import settings
from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.errors.influencer_not_found import InfluencerNotFound
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface
import aiohttp

class YouTubeInfluencerScanner(InfluencerScannerInterface):
    async def scan_channel_id(self, link: str) -> str:
        url = f"https://www.googleapis.com/youtube/v3/search?part=id&type=channel&q={link}&key={settings.YOUTUBE_API_KEY}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if "items" in data and len(data["items"]) > 0:
                    return data["items"][0]["id"]["channelId"]

        raise InfluencerNotFound(link)
    
    async def scan_influencer(self, channel_id: str) -> Influencer:
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={settings.YOUTUBE_API_KEY}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if "items" in data and len(data["items"]) > 0:
                    return Influencer(
                        channel_id, 
                        data["items"][-1]["snippet"]["customUrl"],
                        data["items"][-1]["snippet"]["title"],
                        f"https://www.youtube.com/{data["items"][-1]["snippet"]["customUrl"]}",
                        data["items"][-1]["snippet"]["thumbnails"]["default"]["url"])
                
        raise InfluencerNotFound(channel_id) 
