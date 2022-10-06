from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=90)
texto = "c3r80"
data = image.generate(texto)

image.write(texto, "captcha.png")