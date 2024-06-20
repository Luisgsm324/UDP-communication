from socket import *
from datetime import datetime
import time
import threading
from packages_functions import *

# Socket do client
# AF_INET -> USANDO IPV4
# SOCK_DGRAM -> PROTOCOLO UDP
serverport = 5000
buffer_size = 1024
server = socket(AF_INET, SOCK_DGRAM)
server.bind(("localhost", serverport))

# Armazenar o conteúdo e os autores
queue_content = {
    'adress': [],
    'content': []
}

clients_content = {}

# Armazenar quem está conectado na sessão (pensar um pouco melhor sobre o primeiro dict e essa lista)
clients = []

print(f"Servidor iniciado com sucesso às {datetime.now()}")

def receive_content():
    try:
        with open("receive.txt", mode="w") as file:
            while True:
                output, clientadress = server.recvfrom(buffer_size)
                print(output)
                content = output.decode()    
                
                ip, port = clientadress[0], clientadress[1]
                receive_time = datetime.now()
                
                print("OI")
                data= "awdwadawdwa"
                file.write(data.encode())
                
            
        
    except: print("aaaaaaa")

# def receive_content():
#     try: 
#         while True:
#             output, clientadress = server.recvfrom(buffer_size)

#             content = output.decode()
            
            # ip, port = clientadress[0], clientadress[1]
            # receive_time = datetime.now()
            
            # if content == "/END/":
            #     content = clients_content[clientadress]
            #     if clientadress not in clients:
            #         clients.append(clientadress)
            #         content = f'{content} às {datetime.now()}'
            #         print(content)
            #     else:
            #         name, data = (content.split(":"))[0], (content.split(":"))[1]
            #         if 'bye' not in data:
            #             clients_content[clientadress] = f"{ip}:{port}/~{name}: {data} {receive_time}"
            #         else:
            #             clients_content[clientadress] = f"O usuário {name} saiu da sessão :("
            #             clients.remove(clientadress)
                    
            #     verify_content(clientadress)    
            #     clients_content[clientadress] = ""
            # else:
            #     past_content = clients_content[clientadress] if clientadress in clients_content else ""
#                 clients_content[clientadress] = f"{past_content}{content}"
#     except: pass
            

# fiz essa função para caso a fila sempre seja de tamanho um (caso seja, nem é necessário construir um dicionário, bastam dois parâmetros, mas veremos)
def verify_content(ip):
    content = clients_content[ip]
    if "entrou" in content or 'bye' not in content:
        for client in clients:
            # evita que você mande mensagem para si mesmo (isso faz sentido, mas na cabeça de Vitor é melhor fazer ping-pong)
            # ~Vitor: Cara, vai te ferrar
            if ip != client:
                send_content(content, client)

def send_content(content, adress):
    print(content)
    server.sendto(content.encode(), adress)

while True:
    receive_content()