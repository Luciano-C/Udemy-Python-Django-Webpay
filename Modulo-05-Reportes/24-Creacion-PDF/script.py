from xhtml2pdf import pisa
from jinja2 import Template
import os
from datetime import datetime

ruta = os.path.dirname(os.path.abspath(__file__))
hoy = datetime.today()
timestamp = datetime.timestamp(hoy)



pdf = f"{ruta}/pdf_{timestamp}.pdf"
resultFile = open(pdf, "w+b")


data = {
    "nombre": "Luciano Cabrales",
    "ruta": ruta,
}
sourceHTML = open(os.path.join(ruta, "pdf/ejemplo.html"), encoding="UTF-8").read() 
template = Template(sourceHTML)

html = template.render(data)

pisaStatus = pisa.CreatePDF(html, dest=resultFile)

resultFile.close()