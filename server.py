from socket import *
from datetime import datetime
from packages_functions import *
import os

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
        
        if "saiu da sessão" in content:
            clients.remove(clientadress)
            
        elif "entrou" in content:
            clients.append(clientadress)
        else:
            content = content.replace("/START/", f"{ip}:{port}/~") 
        
        with open("receive.txt", mode="a", encoding='utf-8') as filea:
            print(content, end="")
            filea.write(content.replace("/START/", f"{ip}:{port}/~"))
        
        if "/END/" in content:
            send_packages("", server.sendto, "server", "receive.txt", clientadress, clients)
            print()
            os.remove("receive.txt")
        
    except Exception as e:
        print(f"Error: {e}")

while True:
    receive_content()