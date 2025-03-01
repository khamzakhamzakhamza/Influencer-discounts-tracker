from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface

class YouTubeInfluencerScanner(InfluencerScannerInterface):
    async def scan_username(self, link: str) -> str:
        return "@WeeklyPlanetPodcast"
    
    async def scan_influencer(self, link: str) -> Influencer:
        return Influencer("@WeeklyPlanetPodcast", "Weekly Planet Podcast", "https://www.youtube.com/WeeklyPlanetPodcast", "https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj")
