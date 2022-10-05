import requests

endpoint = "https://rickandmortyapi.com/api/character"
cabecero = {"content-type": "application/json"}
# En ejemplo curso cabecero = {"content-type": "application/json", "token":123456}
# payload = {"nombre": "producto1", "descripcion": "lorem ipsum", "precio": 1234}
# Payload son parámetros que se pasan al request

response = requests.get(endpoint, headers=cabecero)
# response = requests.get(endpoint, headers=cabecero, json=payload)

#print(response.status_code)
print(response.json())