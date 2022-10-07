from stegano import lsb
from stegano import exifHeader
    
# Para png
""" secreto = lsb.hide("black-hole.jpg", "Hola")
secreto.save("imagensecreta.jpg")

lsb.reveal("imagensecreta.jpg") """


# Para jpg
mensaje = "Hello World!"
secret = exifHeader.hide("black-hole.jpg",
                        "imagensecreta.jpg", secret_message=mensaje)
print(exifHeader.reveal("imagensecreta.jpg"))