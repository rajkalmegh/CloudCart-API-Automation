
def test_register_user(api_client):

    data = {
        "username":"testuser",
        "password":"123456"
    }

    response = api_client.post("/register", data)

    assert response.status_code == 200


def test_login_user(api_client):

    data = {
        "username":"testuser",
        "password":"123456"
    }

    response = api_client.post("/login", data)

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_invalid_password(api_client):

    data = {
        "username":"testuser",
        "password":"wrong"
    }

    response = api_client.post("/login", data)

    assert response.status_code == 401
