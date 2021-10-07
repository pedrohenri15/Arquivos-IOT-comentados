# importamos o socket para realizar a conexao e tranferencia dos dados
import socket

# determinamos o destino e a porta de acesso
HOST = 'localhost' # 127.0.0.1
PORT = 5000

# criamos uma varialvel que irá armazenar dos argumentos de soccket, que linka o IPv4 e envia um datagrama. Encerrando a conexao após!
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# variavel que armazena o destino da mensagem 
destino = (HOST, PORT)

# criamos um loop que retorna ao cliente um input para o envio da mensagem. Finalizando mandando a mensagem para o destino
while(True):
    mensagem = bytes(input('Digite a mensagem: '), encoding='utf-8')
    udp.sendto(mensagem, destino)

udp.close()