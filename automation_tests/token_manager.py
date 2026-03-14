
from utils.api_client import APIClient

client = APIClient()

def get_token():

    response = client.post(
        "/login",
        {
            "username": "testuser",
            "password": "123456"
        }
    )

    return response.json()["token"]
