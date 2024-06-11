# video aula 311
# requests para requisições HTTP
import requests

url = 'http://localhost:3333/'
response = requests.get(url)

print(response)
print(response.headers)
print(response.text)
# print(response.json())
