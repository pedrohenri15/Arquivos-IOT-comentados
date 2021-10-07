# importamos o socket para realizar a conexao e tranferencia dos dados
import socket

# determinamos o destino e a porta de acesso
HOST = ''
PORT = 5000

# criamos uma varialvel que irá armazenar dos argumentos de soccket, que linka o IPv4 e envia um datagrama. Encerrando a conexao após!
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# criamos uma variavel para armazenar o acesso
origem = (HOST, PORT)

# ao receber a mensagem o server é ligado e transmite a mensagem do print 
udp.bind(origem)
print("Serviço UDP inicializado. Aguardando mensagem. \n")

# realizamos o loop que recebe dados do socket(cliente) e retorna uma string de ate 1024 bytes, cluindo com o print do cliente e sua mensagem
while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente, msg)

udp.close()

