from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.errors.influencer_not_found import InfluencerNotFound
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface

class MockInfluencerScanner(InfluencerScannerInterface):
    async def scan_channel_id(self, link: str) -> str:
        if link == 'mock_not_found':
            raise InfluencerNotFound(link)
        
        return "channel_id"

    async def scan_influencer(self, link: str) -> Influencer:
        return Influencer("channelId", "@WeeklyPlanetPodcast", "Weekly Planet Podcast", "https://www.youtube.com/WeeklyPlanetPodcast", "https://yt3.googleusercontent.com/v62DJ198S7KshRsMF9Jb6z6MVPuEt3NFXebFbpLZi8KzVvuAlV476Vc_MlXlFJOfDlko3dPXE00=s160-c-k-c0x00ffffff-no-rj")
