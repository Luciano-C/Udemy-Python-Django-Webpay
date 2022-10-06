import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# Use Google Public DNS server to determine own IP
servidor.connect(('8.8.8.8', 80))

print(f"La ip del servidor es {servidor.getsockname()[0]}")

print(f"Nombre de equipo es: {socket.gethostbyname(socket.gethostname())} | {socket.gethostname()}")

servidor.close()