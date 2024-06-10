from socket import *
from datetime import datetime
import time
import threading

# Socket do client
# AF_INET -> USANDO IPV4
# SOCK_DGRAM -> PROTOCOLO UDP
serverport = 5000
buffer_size = 1024
server = socket(AF_INET, SOCK_DGRAM)
server.bind(("", serverport))

# Armazenar o conteúdo e os autores
queue_content = {
    'adress': [],
    'content': []
}

# Armazenar quem está conectado na sessão (pensar um pouco melhor sobre o primeiro dict e essa lista)
clients = []
stop_condition = False

print(f"Servidor iniciado com sucesso às {datetime.now()}")

def receive_content():
    while True:
        output, clientadress = server.recvfrom(buffer_size)
        
        if output.decode() == 'close':
            break
        
        ip, port = clientadress[0], clientadress[1]
        receive_time = datetime.now()
        

        if clientadress not in clients:
            clients.append(clientadress)
            content = output.decode() + f' às {datetime.now()}'
        else:
            name, data = (output.decode().split(":"))[0], (output.decode().split(":"))[1]
            content = f"{ip}:{port}/~{name}: {data} {receive_time}"
        
        print(content, clientadress)
        queue_content['adress'].append(clientadress)
        queue_content['content'].append(content)
        # A função de verificar conteúdo sempre fica no final, então não tem a necessidade de ser um "for" lá
        # validar com o pessoal sobre essa função de verify_content
        verify_content2()

    return stop_condition == True  

# fiz essa função para caso a fila sempre seja de tamanho um (caso seja, nem é necessário construir um dicionário, bastam dois parâmetros, mas veremos)
def verify_content2():
    if queue_content['content'][0] not in 'bye':
        print(clients)
        for client in clients:
            print(client)
            # evita que você mande mensagem para si mesmo (isso faz sentido, mas na cabeça de Vitor é melhor fazer ping-pong)
            if "entrou na sala" not in queue_content['content'][0]:
                if queue_content['adress'][0] != client:
                    send_content(queue_content['content'][0], client)
    # Situação em que o usuário enviou um "bye" e vai ser removido da lista de usuários
    else:
        clients.remove(queue_content['adress'][0])
    # Tirar o conteúdo da fila (tanto de endereço como de conteúdo)
    queue_content['adress'].pop(0)
    queue_content['content'].pop(0)

# essa função foi feita considerando que o dicionário vai encher com mais do que um conteúdo (pela lógica, não aparenta acontecer, mas veremos)
def verify_content():
    for index in range(len(queue_content['adress'])):
        if queue_content['content'][index] != 'bye':
            print(clients)
            for client in clients:
                print(client)
                if "entrou na sala" not in queue_content['content'][index]:
                    if queue_content['adress'][index] != client:
                        send_content(queue_content['content'][index], queue_content['adress'][index])
                else:
                    send_content(queue_content['content'][index], queue_content['adress'][index])  
                # O client escreveu 'bye' e vai ser removido tanta da lista de clients
        else:
            clients.remove(queue_content['adress'][index])
        queue_content['adress'].pop(index)
        queue_content['content'].pop(index)

def send_content(content, adress):
    server.sendto(content.encode(), adress)

while True:
    receive_content()
    if stop_condition:
        break