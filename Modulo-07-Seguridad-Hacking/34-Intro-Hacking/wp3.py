import json
import urllib.request
"""
Lista de usuarios:
Usualmente páginas wordpress muestran sus usuarios con la terminación wp-json/wp/v2/users
En este caso, no resultó
"""
url = "http://localhost/clientes/tamila/clientes/pruebas/wordpress_dev/gym"

with urllib.request.urlopen(url) as response:
    html = response.read()
    for u in json.loads(html):
        print(u["slug"])