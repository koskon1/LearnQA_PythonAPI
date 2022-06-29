import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects= True)
first_response = response.history
second_response = response


print(first_response.__len__())
print(second_response.url)

