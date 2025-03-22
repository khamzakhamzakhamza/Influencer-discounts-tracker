import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock
from idt_scrapper.config import settings
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.services.content_service import ContentService
from tests.shared.builders.content_builder import ContentBuilder
from tests.shared.builders.influencer_builder import InfluencerBuilder

@pytest.fixture
def content_service():
    mock_repo = MagicMock(spec=ContentRepositoryInterface)
    mock_scanner = MagicMock(spec=ContentScannerInterface)

    service = ContentService(mock_repo, mock_scanner)
    return service, mock_repo, mock_scanner

def test_delete_stale_when_should_filter_stale_content(content_service):
    # Arrange
    influencer = InfluencerBuilder().build()
    configured_period = settings.CONTENT_PERIOD_DAYS

    valid_date = datetime.now(timezone.utc) - timedelta(days=configured_period - 1)
    stale_date = datetime.now(timezone.utc) - timedelta(days=configured_period)

    valid_content = ContentBuilder().with_id('valid').with_content_creation_date(valid_date).build() 
    stale_content = ContentBuilder().with_id('stale').with_content_creation_date(stale_date).build()
    content = [ valid_content, stale_content ]

    service, mock_repo, _ = content_service
    mock_repo.get_content.return_value = content

    # Act
    service.delete_stale(influencer)
    
    # Assert
    mock_repo.delete_content.assert_called_once_with([ valid_content.id ])