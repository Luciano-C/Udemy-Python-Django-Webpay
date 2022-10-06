import requests
from bs4 import BeautifulSoup

"""Captura el tema de una página de wordpress"""
url = "http://localhost/clientes/tamila/clientes/pruebas/wordpress_dev/gym"
headers = {"User-Agent": "Firefox"}
peticion = requests.get(url=url, headers=headers)
soup = BeautifulSoup(peticion.text, "html.parser")
for enlace in soup.find_all("link"):
    if("/wp-content/themes") in enlace.get("href"):
        the = enlace.get("href")
        the.split("/")
        if "themes" in the:
            pos = the.index("themes")
            theme = the[pos + 1]
            print(theme)