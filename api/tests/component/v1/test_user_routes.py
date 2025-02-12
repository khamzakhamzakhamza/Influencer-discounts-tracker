def post_user_should_call_dependencies(client):
    username="test"
    
    response = client.post("/api/v1/users", json={"username": username})
    
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["username"] == username
