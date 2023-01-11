import requests

payload={"name": "Skvosh56"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)
