from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface

class InfluencerService:
    def __init__(self, influencer_repository: InfluencerRepositoryInterface, influencer_scanner: InfluencerScannerInterface):
        self.influencer_repository = influencer_repository
        self.influencer_scanner = influencer_scanner
    
    async def create_and_associate_influencer(self, username: str, link: str) -> Influencer:
        influencer_username = await self.influencer_scanner.scan_username(link)
        influencer = await self.influencer_repository.get_influencer(influencer_username)

        if influencer is None:
            influencer = await self.influencer_scanner.scan_influencer(link)
            await self.influencer_repository.create_influencer(influencer)
        
        await self.influencer_repository.associate_user(influencer, username)

        return influencer
