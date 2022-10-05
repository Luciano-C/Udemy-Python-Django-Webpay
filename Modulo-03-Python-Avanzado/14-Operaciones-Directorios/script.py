import os
import shutil

ruta = os.path.dirname(os.path.abspath(__file__))
#print(ruta)


archivo_actual = os.path.abspath(__file__)
#print(archivo_actual)

directorio_de_trabajo = os.getcwd()
#print(directorio_de_trabajo)

# Crea carpeta. El / adelante es importante, sino crea la carpeta en una ruta diferente
if not os.path.isdir(ruta + "/micarpeta"):
    os.makedirs(ruta + "/micarpeta")

# Lista de archivos y directorios
#print(os.listdir(ruta))

# Cambia nombre
os.rename(ruta + "/micarpeta", ruta + "/micarpetamodificada")

# Elimina carpeta
os.rmdir(ruta + "/micarpetamodificada")

# Borrar una carpeta que no está vacía
if os.path.isdir(ruta + "/test"):
    shutil.rmtree(ruta + "/test")

#shutil.copy(ruta + "/hola.html", ruta + "/holaychao.html")
shutil.move(ruta + "/hola.html", ruta + "/holaychao.html")