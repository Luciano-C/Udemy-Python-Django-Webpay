import json
import os

ruta = os.path.dirname(os.path.abspath(__file__))

data = {}

data["post"] = []

for i in range(1,11):
    data["post"].append(
        {
            "id": i,
            "titulo": f"Título de la publicación {i}",
            "slug": f"titulo-de-la-publicacion-{i}",
            "detalle": f"Texto de detalle con ñandú {i}",
            "fecha": "2022-04-30"
        }
    )

with open(ruta + "/ejemplo.json", "w") as file:
    json.dump(data, file, indent=4)
