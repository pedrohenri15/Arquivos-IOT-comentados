# importa paho no mqtt
import paho.mqtt.client as mqtt
# importamos instruçoes de tempo 
import time
# importamos instruçoes de json-formataçao
import json

#  esta sendo criado uma instancia do objeto e nomeando o cliente
client = mqtt.Client(client_id='devpy')
client = mqtt.Client(client_id='sub-py')

# conexao do cliente ao broker
client.connect('localhost', port=1883)

#  cliente escreve o caminho para os recursos do servidor
client.subscribe('casa/sala/lampada/1')

# client.subscribe('casa/sala/lampada/1/intensidade')
print("Subscriber connected!")

# funçao que de forma assincrona tras as informaçoes do programa como resposta
def on_message_callback(client, userdata, message):
    # variavel que armazena a formaracao da mensagem 
    msg = json.loads(message.payload.decode('utf-8'))

    if(msg["status"] == True):
        # Liga pino do raspberry / arduino
        print("Pino X ligado")
    elif(msg["status"] == False):
        # Desliga pino do raspberry / arduino
        print("Pino X desligado")


    # print(message.payload.decode('utf-8'))
client.on_message = on_message_callback
client.loop_forever()
