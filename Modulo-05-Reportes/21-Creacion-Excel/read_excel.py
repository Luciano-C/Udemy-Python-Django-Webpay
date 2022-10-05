import xlrd
import os
import pandas as pd

ruta = os.path.dirname(os.path.abspath(__file__))
documento = xlrd.open_workbook(ruta + "/archivo.xlsx")
datos = documento.sheet_by_index(0)
print(documento)

for i in range(datos.nrows):
    if i >= 1:
        print(f"ID={datos.cell_value(i,0)} | Nombre: {datos.cell_value(i,1)} | Apellido: {datos.cell_value(i,2)}")


# xlrd no parece ser necesario, se podría cargar el archivo usand pandas

df = pd.read_excel(ruta + "/archivo.xlsx", sheet_name="Hoja 1")

print(df) 
