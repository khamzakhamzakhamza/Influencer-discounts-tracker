import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock
from idt_scrapper.config import settings
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface
from idt_scrapper.domain.services.influencer_service import InfluencerService
from tests.shared.builders.content_builder import ContentBuilder
from tests.shared.builders.influencer_builder import InfluencerBuilder

@pytest.fixture
def influencer_service():
    mock_repo = MagicMock(spec=InfluencerRepositoryInterface)
    mock_scanner = MagicMock(spec=InfluencerScannerInterface)

    service = InfluencerService(mock_repo, mock_scanner)
    return service, mock_repo, mock_scanner

def test_get_influencers_to_update_should_filter_updated_influencers(influencer_service):
    # Arrange
    updated_influencer = InfluencerBuilder().with_last_update_date(datetime.now(timezone.utc)).build()
    new_influencer = InfluencerBuilder().with_channel_id('new').with_last_update_date(datetime.now(timezone.utc) - timedelta(days=1)).build()

    service, mock_repo, _ = influencer_service
    mock_repo.get_influencers_by_desc_update_date.return_value = [updated_influencer, new_influencer]
    
    # Act
    result = service.get_influencers_to_update()
    
    # Assert
    assert len(result) == 1
    assert result[0].channel_id == new_influencer.channel_id
    mock_repo.get_influencers_by_desc_update_date.assert_called_once()

