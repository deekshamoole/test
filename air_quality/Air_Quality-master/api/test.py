import requests

headers = {"X-API-Key": "621b301f86a274ae03114faf9404d2d126637646811a760c949d39607af92296"}  # replace this


url = "https://api.openaq.org/v3/locations/8118"


response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())