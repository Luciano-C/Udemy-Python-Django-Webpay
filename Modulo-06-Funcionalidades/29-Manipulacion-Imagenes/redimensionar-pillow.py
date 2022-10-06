from PIL import Image

def redimensionar():
    image = Image.open("black-hole.jpg")
    image.thumbnail((90, 90))
    image.save("black-hole-resized-pillow.jpg")

redimensionar()