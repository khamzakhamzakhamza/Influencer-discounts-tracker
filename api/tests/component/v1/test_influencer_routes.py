from tests.shared.utils import is_valid_guid

def test_post_influencer_should_create_new_influencer(client):
    username="test"
    link="https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw"
    
    client.post("/api/v1/users", json={"username": username})
    response = client.post("/api/v1/influencers", json={"username": username, "link": link})
    
    assert response.status_code == 200
    assert response.json()["username"] == "@WeeklyPlanetPodcast"
    assert is_valid_guid(response.json()["id"]) is True
