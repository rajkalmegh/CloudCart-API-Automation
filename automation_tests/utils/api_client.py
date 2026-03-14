
import requests
from utils.config import BASE_URL

class APIClient:

    def get(self, endpoint, headers=None):
        requests.get(BASE_URL + endpoint, headers=headers, verify=False)

    def post(self, endpoint, data=None, headers=None):
        return requests.post(BASE_URL + endpoint, json=data, headers=headers)
