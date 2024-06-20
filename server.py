from socket import *
from datetime import datetime
from packages_functions import *

# Socket do client
# AF_INET -> USANDO IPV4
# SOCK_DGRAM -> PROTOCOLO UDP
serverport = 5000
buffer_size = 1024
server = socket(AF_INET, SOCK_DGRAM)
server.bind(("localhost", serverport))

# Armazenar quem está conectado na sessão (pensar um pouco melhor sobre o primeiro dict e essa lista)
clients = []

print(f"Servidor iniciado com sucesso às {datetime.now()}")


def receive_content():
    try:
        output, clientadress = server.recvfrom(buffer_size)
        content = output.decode()    
                    
        ip, port = clientadress[0], clientadress[1]
        receive_time = datetime.now()
        
        if "bye" in content:
            content = f"O usuário {name} saiu da sessão :("
            clients.remove(clientadress)
        elif "entrou" in content:
            content = f'{content} às {receive_time}'
            clients.append(clientadress)
        else:
            name, data = (content.split(":"))[0], (content.split(":"))[1]
            content = f"{ip}:{port}/~{name}: {data} {receive_time}"
            
        
        send_packages(content, server.sendto, "server", "receive.txt", clientadress, clients)
        
    except Exception as e:
        print(f"Error: {e}")

while True:
    receive_content()