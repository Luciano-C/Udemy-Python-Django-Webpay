import qrcode

img = qrcode.make("https://www.lucianocabrales.com/")

f = open("qr.png", "wb")
img.save(f)
f.close()