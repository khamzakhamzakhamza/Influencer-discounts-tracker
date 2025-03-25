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

def test_delete_stale_should_filter_stale_content(content_service):
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

def test_delete_stale_should_return_most_recent_date(content_service):
    # Arrange
    influencer = InfluencerBuilder().build()
    date = datetime.now(timezone.utc)
    expected_date = datetime.now(timezone.utc) + timedelta(days=1)

    # assuming that repository returns ordered content
    content = [
        ContentBuilder().with_content_creation_date(expected_date).build(),
        ContentBuilder().with_content_creation_date(date).build()
    ]

    service, mock_repo, _ = content_service
    mock_repo.get_content.return_value = content

    # Act
    actual_date = service.delete_stale(influencer)
    
    # Assert
    assert actual_date == expected_date

def test_delete_stale_when_all_stale_should_return_none(content_service):
    # Arrange
    influencer = InfluencerBuilder().build()
    configured_period = settings.CONTENT_PERIOD_DAYS
    date = datetime.now(timezone.utc) - timedelta(days=configured_period - 1)
    most_recent_date = datetime.now(timezone.utc) - timedelta(days=configured_period)

    # assuming that repository returns ordered content
    content = [
        ContentBuilder().with_content_creation_date(most_recent_date).build(),
        ContentBuilder().with_content_creation_date(date).build()
    ]

    service, mock_repo, _ = content_service
    mock_repo.get_content.return_value = content

    # Act
    actual_date = service.delete_stale(influencer)
    
    # Assert
    assert actual_date is None

