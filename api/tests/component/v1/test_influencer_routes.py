from tests.shared.utils import is_valid_guid

def test_post_influencer_should_create_new_influencer(client):
    # Arrange
    username="test"
    link="https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw"
    
    # Act
    client.post("/api/v1/users", json={"username": username})
    response = client.post("/api/v1/influencers", json={"username": username, "link": link})
    
    # Assert
    assert response.status_code == 200
    assert response.json()["username"] == "@WeeklyPlanetPodcast"
    assert is_valid_guid(response.json()["id"]) is True

def test_post_influencer_should_return_not_found(client):
    # Arrange
    username="test"
    link="mock_not_found"
    
    # Act
    client.post("/api/v1/users", json={"username": username})
    response = client.post("/api/v1/influencers", json={"username": username, "link": link})
    
    # Assert
    assert response.status_code == 404
    assert response.json()["code"] == 1000

def test_get_influencers_should_return_user_influencers(client):
    # Arrange
    username="test"
    link="https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw"

    # Act
    client.post("/api/v1/users", json={"username": username})
    client.post("/api/v1/influencers", json={"username": username, "link": link})
    response = client.get(f"/api/v1/influencers?username={username}")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["username"] == "@WeeklyPlanetPodcast"

