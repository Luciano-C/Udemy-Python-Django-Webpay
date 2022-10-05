from suds.client import Client

endpoint = "https://www.w3.org/2003/05/soap-envelope/"

cliente = Client(endpoint)

#print(cliente)

"""

En ejemplo usa otro endpoint que ya no existe
resultado = cliente.service.retornarDatos("Cesar Cancino", "yo@cecarcancino.com", "+5691234567" )
print(resultado)

Se ve en consola de la siguiente manera:
Nombre=Cesar Cancino
Telefono=+5691234567
Email=yo@cecarcancino.com

El método retornarDatos fue definido por el autor de la Api


"""