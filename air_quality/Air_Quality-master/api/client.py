import requests
from config import BASE_URL, API_KEY

HEADERS = {"X-API-Key": API_KEY}

class OpenAQClient:
    def __init__(self):
        self.measurements_url = BASE_URL

    def fetch_all_data(self):
        params = {"limit": 1000}
        response = requests.get(self.measurements_url, params=params, headers=HEADERS)
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
        return [response.json()]  # return list to match loader expectations