import argparse

parser = argparse.ArgumentParser(description="Ejemplo de argparse")

parser.add_argument('-s', '--server', help="Servidor")

# python archivo.py --s hola

args = parser.parse_args()

if args.server:
    print(args.server)
else:
    print("No se recibió el nombre del server")