import requests

response = requests.get(url="https://onet.eu")
print(response.text)