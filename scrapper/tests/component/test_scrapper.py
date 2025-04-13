def test_update_influencers_should_update_influencers(scrapper_fixture):
    # Arrange
    expected_id = "https://yt3.ggpht.com/uNnYRnCNiXwSx3IZcJoV0fRmDlTQIsIu4rHsGWvLSjGslrv-D4m1bUO6c7-0zoU4J8ol-9OrNvo=s88-c-k-c0x00ffffff-no-rj"

    # Act
    updated_ids = scrapper_fixture.update_influencers()
    
    # Assert
    assert len(updated_ids) > 0, "No influencers were updated"
    assert expected_id in updated_ids, f"Expected ID {expected_id} not found in updated IDs"
