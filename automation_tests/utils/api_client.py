import requests
import urllib3
from utils.config import BASE_URL

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APIClient:

    def get(self, endpoint, headers=None):
        return requests.get(
            BASE_URL + endpoint,
            headers=headers,
            verify=False
        )

    def post(self, endpoint, data=None, headers=None):
        return requests.post(
            BASE_URL + endpoint,
            json=data,
            headers=headers,
            verify=False
        )
