from fastapi import Depends
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_api.domain.repositories.user_repository_interface import UserRepositoryInterface
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface
from idt_api.domain.services.influencer_service import InfluencerService
from idt_api.domain.services.user_service import UserService
from idt_api.infrastructure.dependencies import get_influencer_repository, get_influencer_scanner, get_user_repository

def get_user_service(user_repo: UserRepositoryInterface = Depends(get_user_repository)):
    return UserService(user_repo)

def get_influencer_service(influencer_repo: InfluencerRepositoryInterface = Depends(get_influencer_repository), influencer_scanner: InfluencerScannerInterface = Depends(get_influencer_scanner)):
    return InfluencerService(influencer_repo, influencer_scanner)
