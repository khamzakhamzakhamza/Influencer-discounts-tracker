import pytest
from unittest.mock import AsyncMock, MagicMock
from idt_api.domain.entities.influencer import Influencer
from idt_api.domain.entities.user import User
from idt_api.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_api.domain.scanner.influencer_scanner_interface import InfluencerScannerInterface
from idt_api.domain.services.influencer_service import InfluencerService

@pytest.fixture
def influencer_service():
    mock_repo = MagicMock(spec=InfluencerRepositoryInterface)
    mock_scanner = MagicMock(spec=InfluencerScannerInterface)

    mock_scanner.scan_channel_id = AsyncMock()
    mock_scanner.scan_influencer = AsyncMock()
    mock_repo.get_influencer = AsyncMock()
    mock_repo.create_influencer = AsyncMock()
    mock_repo.associate_user = AsyncMock()

    service = InfluencerService(mock_repo, mock_scanner)
    return service, mock_repo, mock_scanner

@pytest.mark.asyncio
async def test_create_and_associate_influencer_should_return_existing_influencer(influencer_service):
    # Arrange
    expected_user = User("John Doe")
    expected_influencer = Influencer("channelId", "test", "Test", "https://www.test.com", "https://www.test.com/image.jpg")
    
    service, mock_repo, mock_scanner = influencer_service
    mock_scanner.scan_channel_id.return_value = expected_influencer.username
    mock_repo.get_influencer.return_value = expected_influencer

    # Act
    influencer = await service.create_and_associate_influencer(expected_user, expected_influencer.channelUrl)
    
    # Assert
    assert influencer is not None
    assert influencer == expected_influencer
    mock_scanner.scan_influencer.assert_not_called()
    mock_repo.create_influencer.assert_not_called()
    mock_repo.associate_user.assert_called_once_with(expected_influencer, expected_user)

@pytest.mark.asyncio
async def test_create_and_associate_influencer_should_create_influencer(influencer_service):
    # Arrange
    expected_user = User("John Doe")
    expected_influencer = Influencer("channelId", "test", "Test", "https://www.test.com", "https://www.test.com/image.jpg")
    
    service, mock_repo, mock_scanner = influencer_service
    mock_scanner.scan_channel_id.return_value = expected_influencer.username
    mock_repo.get_influencer.return_value = None
    mock_scanner.scan_influencer.return_value = expected_influencer

    # Act
    influencer = await service.create_and_associate_influencer(expected_user, expected_influencer.channelUrl)
    
    # Assert
    assert influencer is not None
    assert influencer == expected_influencer
    mock_repo.create_influencer.assert_called_once_with(expected_influencer)
    mock_repo.associate_user.assert_called_once_with(expected_influencer, expected_user)
