# importamos o socket para realizar a conexao e tranferencia dos dados
import socket

# determinamos o destino e a porta de acesso 
HOST = ''
PORT = 5000

# criamos uma varialvel que irá armazenar dos argumentos de soccket, que linka o IPv4 e TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# criamos uma variavel para armazenar o acesso 
origem = (HOST, PORT)

# ao iniciar o server a variavel tcp liga e escuta e atraves do print informa o inicio da conexao do servidor
tcp.bind(origem)
tcp.listen(1)
print('Serviço iniciado')


# crimos o loop para mostrar o cliente e sua mensagem ao conectar-se ao servidor 
while(True):
    con, cliente = tcp.accept()
    print("Conectado por", cliente)
    while(True):
        mensagem = con.recv(1024)
        print(cliente, mensagem)

con.close()