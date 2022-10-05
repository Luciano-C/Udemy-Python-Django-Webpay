from PyPDF2 import PdfFileMerger

pdfs = ["pdf_1.pdf", "pdf_2.pdf", "pdf_3.pdf"]

nombre_salida = "salida.pdf"

fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, "rb"))

with open (nombre_salida, "wb") as salida:
    fusionador.write(nombre_salida)