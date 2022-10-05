import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

""" 
Los correos deben venir de un hosting con proveedor de correo. Por ahora se usarán los del video.
"""

def send_mail():
    fromaddr = "info@villancino.cl"
    toaddr = "info@tamila.cl"
    password = "password_villancino"
    asunto = "Correo de aviso de pago"
    html = """
    <html>
        <head></head>
        <body>
            <h1>Mensaje desde Python</h1>
            <p>Hola ñandú</p>
        </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = asunto

    msg.attach(MIMEText(html, "html"))

    # Archivo adjunto
    filename = "pdf_1.pdf"
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(part)



    # smpt.deamhost.com: Nombre smpt del servidor, no siempre tienen esa estructura
    # 587: Puerto del servidor
    server = smtplib.SMTP('smtp.deamhost.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()



