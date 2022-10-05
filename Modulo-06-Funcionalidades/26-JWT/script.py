# El modulo para importar jwt es pyjwt
import jwt
import time 


secreto = "L6y@42C3^aJU"
ts = int(time.time())
payload = {"id": 1, "nombre": "Pepito", "time": ts}


token = jwt.encode(payload, secreto, algorithm="HS256")
print(token)

resuelto = jwt.decode(token, secreto, algorithms=["HS256"])
print(resuelto)

