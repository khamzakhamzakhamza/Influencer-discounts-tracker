from datetime import datetime, timedelta, timezone
from tests.shared.builders.affiliated_link_builder import AffiliatedLinkBuilder
from tests.shared.builders.content_builder import ContentBuilder
from tests.shared.builders.influencer_builder import InfluencerBuilder

def test_update_influencers_should_update_influencers(scrapper_fixture):
    # Arrange
    influencer_repo_mock, content_repo_mock, content_scanner_mock, affiliated_link_repo_mock, affiliated_link_scanner_mock, scrapper = scrapper_fixture

    expected_influencer = InfluencerBuilder().with_last_update_date(datetime.now(timezone.utc) - timedelta(days=1)).build()
    influencer_repo_mock.get_influencers_by_desc_update_date.return_value = [expected_influencer]

    expected_content = ContentBuilder().with_content_creation_date(datetime.now(timezone.utc) - timedelta(days=2)).build()
    content_repo_mock.get_content.side_effect = lambda inf: [expected_content] if inf == expected_influencer else []

    new_content = ContentBuilder().with_content_creation_date(datetime.now(timezone.utc) - timedelta(days=1)).build()
    content_scanner_mock.scan_content.side_effect = lambda inf, _: [new_content] if inf == expected_influencer else []

    expected_affiliated_link = AffiliatedLinkBuilder().build()
    affiliated_link_scanner_mock.scan_links.side_effect = lambda content: [expected_affiliated_link] if content == new_content else []

    # Act
    updated_ids = scrapper.update_influencers()
    
    # Assert
    assert len(updated_ids) > 0, "No influencers were updated"
    assert expected_influencer.id in updated_ids, f"Expected ID {expected_influencer.id} not found in updated IDs"
    
    content_repo_mock.delete_content.assert_called_with([])
    content_repo_mock.save_content.assert_called_with(expected_influencer, [new_content])

    affiliated_link_repo_mock.save_links.assert_called_with(new_content, [expected_affiliated_link])
