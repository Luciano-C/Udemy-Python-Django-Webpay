import cv2
import os


ruta = os.path.dirname(os.path.abspath(__file__))
src = cv2.imread(ruta + "/black-hole.jpg", cv2.IMREAD_UNCHANGED)

porcentaje = 50

width = int(src.shape[1] * porcentaje / 100)
height = int(src.shape[0] * porcentaje / 100)

dsize = (width, height)

output = cv2.resize(src, dsize)

cv2.imwrite(ruta + "/black-hole-resized.jpg", output)


