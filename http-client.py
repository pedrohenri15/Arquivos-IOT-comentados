# import http.client

# http.client.HTTPConnection(host)

# para o http.cliente impotamos a classe de conexao ao server
from http.client import HTTPConnection

# criamos uma variavel que armazena a conexao do cliente com o server 
conexao = HTTPConnection('localhost:5000')

# cliente solicita a conexao ao GET
conexao.request("GET", "/")

# variavel que armazena a resposta do server 
resposta = conexao.getresponse()

# variavel que armazena a leitura da resposta e logo o print para a resposts
pagina = resposta.read()
print(pagina)