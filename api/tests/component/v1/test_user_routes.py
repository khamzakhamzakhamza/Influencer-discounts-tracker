from tests.shared.utils import is_valid_guid

def test_post_user_should_call_dependencies(client):
    username="test"
    
    response = client.post("/api/v1/users", json={"username": username})
    
    assert response.status_code == 200
    assert response.json()["username"] == username
    assert is_valid_guid(response.json()["id"]) is True
