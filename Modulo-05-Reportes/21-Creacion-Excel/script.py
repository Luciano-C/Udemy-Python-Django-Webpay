import pandas as pd
import os

ruta = os.path.dirname(os.path.abspath(__file__))

datos = pd.DataFrame({
    "id": [1,2,3,4],
    "nombre": ["Juan", "Yelimar", "María", "Pedro"],
    "apellido": ["Martínez", "Pérez", "Barceló", "Mondaca"]
})

with pd.ExcelWriter(ruta + "/archivo.xlsx") as writer:
    datos.to_excel(writer, sheet_name="Hoja 1", index=False)

