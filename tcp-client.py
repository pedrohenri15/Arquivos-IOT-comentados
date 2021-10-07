# importamos o socket para realizar a conexao e tranferencia dos dados
import socket

# determinamos o destino e a porta de acesso
HOST = 'localhost'
PORT = 5000

# criamos uma varialvel que irá armazenar dos argumentos de soccket, que linka o IPv4 e TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# criamos uma variavel para armazenar o local do acesso
destino = (HOST, PORT)

# a conexao tcp com o server 
tcp.connect(destino)

# criamos o loop while para retornar ao cliente atraves do input a mensagem que deseja enviar ao servidor 
while(True):
    mensagem = bytes(input("Digite a mensagem: "), encoding='utf-8')

# manda a mensagem
    tcp.send(mensagem)

# finaliza 
    tcp.close()