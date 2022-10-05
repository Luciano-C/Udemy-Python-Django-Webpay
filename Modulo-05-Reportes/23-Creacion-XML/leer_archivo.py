from xml.dom import minidom
import os

ruta = os.path.dirname(os.path.abspath(__file__))

xml = minidom.parse(ruta + "/ejemplo.xml")

docs = xml.getElementsByTagName("doc")

for doc in docs:
    nodo1 = doc.getElementsByTagName("nodo1")[0]
    nodo2 = doc.getElementsByTagName("nodo2")[0]
    print(f"Nodo1={nodo1.firstChild.data} | Nodo2={nodo2.firstChild.data}")
    