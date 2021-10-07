# importa o paho e nomeia o protocolo como mqtt
import paho.mqtt.client as mqtt

# variavel (BROKER) local constante e variavel (PORT) porta utilizada
BROKER = "Localhost"
PORT = 1883

# variavel que armazena quem acessa o server 
client = mqtt.Client("pubpy")

# conexao no broker e na porta
client.connect(BROKER, PORT)

# funcao que responde 
def on_publish_callbck(client, userdata, result):
    print("Dado publicado")

# 1ª variavel start a 2ª que chama a funçao e printa a mensagem 
client.on_publish = on_publish_callbck


#Recebe o input e apresenta a resposta atraves do loop
while(True):
    value = input("Digite 1 para ligado ou 0 para desligado")
    status = "false"
    if (value == "0"):
        status = "false"
    elif(value == "1"):
        status = "true"

#  possui o topico e a mensagem (str), usando a funcao para formatar e expressar a str corretamente 
    client.publish('casa/sala/lampada/1', '{"status": %s}' % str(status))
    print('{"status : %s}' % str(status))