import xml.etree.cElementTree as ET
import os

ruta = os.path.dirname(os.path.abspath(__file__))

root = ET.Element("root")

for numero in range(1, 4):
    doc = ET.SubElement(root, "doc")
    ET.SubElement(doc, "nodo1", name="nodo").text = f"Texto nodo1 {numero}"
    ET.SubElement(doc, "nodo2", atributo="manzana").text = f"Texto nodo2 {numero}"


archivo = ET.ElementTree(root)
archivo.write(ruta + "/ejemplo.xml") 

""" 
Archivo XML a crear
<root>
    <doc>
        <nodo1 name="nodo">Texto nodo1 0</nodo1>
        <nodo2 atributo="manzana">Texto nodo2 0</nodo2>
    </doc>
</root>

 """
