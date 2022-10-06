from barcode import EAN13
from barcode.writer import ImageWriter
import os

ruta = os.path.dirname(os.path.abspath(__file__))

# Número de 12 caracteres para EAN13
numero = "111111111111"

mi_codigo = EAN13(numero, writer=ImageWriter)
mi_codigo.save(ruta + "/barra")

