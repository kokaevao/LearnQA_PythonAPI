import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first_response = response.history
second_response = response

print(len(first_response))
print(second_response.url)
