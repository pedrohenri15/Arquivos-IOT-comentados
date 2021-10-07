# importamos do pacote http.server as classes prontas, para manipular e perguntas e respostas
from http.server import BaseHTTPRequestHandler, HTTPServer

# determinamos o destino e a porta de acesso
HOST = 'localhost'
PORT = 5000

# classe myhandler que extende uma outra classe feita para manipular requisicao 
class MyHandler(BaseHTTPRequestHandler):

# serve para resonder uma requisao GET, responde o cliente, formatamos e escrevemos o arquivo HTML para enviar ao cliente
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>AULA HTTP</title></head>", 'utf-8'))
        self.wfile.write(bytes("<body>", 'utf-8'))
        self.wfile.write(bytes("<p><SERVIDOR HTTP de exemplo.</p>", 'utf-8'))
        self.wfile.write(bytes("</body></html>",  'utf-8'))

# criamos a varialvel que armazena o server, o destino da mensagem e a configuraçao do myhandler
webServer = HTTPServer((HOST,PORT), MyHandler)

# print da mensagem enviada ao cliente
print("Servidor iniciado em http://%s:%s" % (HOST, PORT))

# loop eterno de resposta ao cliente
webServer.serve_forever()