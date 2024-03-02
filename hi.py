# Importar el módulo http.server para crear el servidor web
import http.server
import socketserver

# Establecer el puerto en el que se ejecutará el servidor
PORT = 8000

# Clase para manejar las solicitudes HTTP
class MiHandler(http.server.SimpleHTTPRequestHandler):
    # Este método se ejecuta cada vez que se recibe una solicitud GET
    def do_GET(self):
        # Enviar la respuesta HTTP con el código de estado 200 (OK)
        self.send_response(200)
        # Establecer las cabeceras para indicar que el contenido es de tipo HTML
        self.send_header("Content-type", "text/html")
        # Finalizar las cabeceras
        self.end_headers()
        # Enviar el contenido HTML de respuesta
        self.wfile.write(b"<html><head><title>Mi servidor web</title></head>")
        self.wfile.write(b"<body><h1>Hola Mundo!</h1></body></html>")

# Crear el servidor web con el manejador personalizado
with socketserver.TCPServer(("", PORT), MiHandler) as httpd:
    print("Servidor activo en el puerto:", PORT)
    # Esperar y manejar las solicitudes entrantes de manera indefinida
    httpd.serve_forever()

