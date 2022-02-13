from urllib import response
import requests

print('hello sexy?')

response = requests.get("https://www.naver.com")
html = response.text
print(html)