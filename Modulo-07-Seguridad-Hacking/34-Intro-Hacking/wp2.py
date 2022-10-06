import requests
from bs4 import BeautifulSoup

"""Captura la versión de wordpress de una página de wordpress"""
url = "http://localhost/clientes/tamila/clientes/pruebas/wordpress_dev/gym"

headers = {"User-Agent": "Firefox"}
peticion = requests.get(url=url, headers=headers)
soup = BeautifulSoup(peticion.text, "html.parser")
for v in soup.find_all("meta"):
    if v.get("name") == "generator":
        version = v.get("content")
        print(version)