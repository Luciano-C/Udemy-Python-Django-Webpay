import requests
import re

url = "http://localhost/clientes/tamila/clientes/pruebas/scrap.php"

response = requests.get(url)

if response.status_code== 200:
	content = response.text
	#<div class="price">$4248</div>
	regex = '<div class="price">(.+?)</div>'
	for precio in re.findall(regex, content):
		print(f"el precio es {precio[1:len(precio)]}")
else:
	print("no puedo hacer el proceso voy a llorar!!")

    