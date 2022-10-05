import json
import os

ruta = os.path.dirname(os.path.abspath(__file__))

with open(ruta + "/ejemplo.json") as file:
    datos = json.load(file)

for dato in datos["post"]:
    print(f"Id={dato['id']}\nTítulo={dato['titulo']}\nslug={dato['slug']}\ndetalle={dato['detalle']}\nfecha={dato['fecha']}")
    print("-" * 50)
