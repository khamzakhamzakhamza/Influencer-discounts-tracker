def test_update_influencers_should_update_influencers(scrapper_fixture):
    # Arrange
    username="test"
    
    # Act
    scrapper_fixture.update_influencers()
    
    # Assert
