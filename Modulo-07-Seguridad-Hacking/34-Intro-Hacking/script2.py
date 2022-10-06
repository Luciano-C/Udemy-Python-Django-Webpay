import requests

obj = requests.get("http://cesarcancino.com")

headers = dict(obj.headers)

print(headers)