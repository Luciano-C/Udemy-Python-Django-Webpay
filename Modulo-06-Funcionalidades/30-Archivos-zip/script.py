import zipfile
import os

ruta = os.path.dirname(os.path.abspath(__file__))

archivo = zipfile.ZipFile(ruta + "/archivo.zip", "w")
archivo.write("black-hole.jpg", compress_type=zipfile.ZIP_DEFLATED)
archivo.close()
