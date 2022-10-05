import wsgiref
from jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server
import os

def desplegar_app(environment, start_response):
    ruta = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(ruta + "/templates"))
    template = env.get_template("ejemplo.html")

    data = {
        "titulo": "Hola mundo",  
    }
    html = template.render(data)
    headers = [("Content-type", "text/html; charset=utf-8")]
    
    start_response("200 OK", headers)

    return [bytes(html, "utf-8")]


server = make_server("localhost", 8003, desplegar_app)
server.serve_forever()