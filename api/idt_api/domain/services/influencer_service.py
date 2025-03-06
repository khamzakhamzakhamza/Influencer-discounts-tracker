from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface

class InfluencerService:
    def __init__(self, influencer_repository: InfluencerRepositoryInterface, influencer_scanner: InfluencerScannerInterface):
        self.influencer_repository = influencer_repository
        self.influencer_scanner = influencer_scanner
    
    async def create_and_associate_influencer(self, user: User, link: str) -> Influencer:
        channel_id = await self.influencer_scanner.scan_channel_id(link)
        influencer = await self.influencer_repository.get_influencer(channel_id)

        if influencer is None:
            influencer = await self.influencer_scanner.scan_influencer(channel_id)
            await self.influencer_repository.create_influencer(influencer)
        
        await self.influencer_repository.associate_user(influencer, user)

        return influencer
