from socket import *
from datetime import datetime
from packages_functions import *
from classes.StateMachine import *
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

transmiter_state_machine = TransmiterStateMachine(server, buffer_size, "server", "receive.txt")
receiver_state_machine = ReceiverStateMachine(server, buffer_size, "server", "receive.txt")

def receive_content():
    # try:
        output, clientaddress = server.recvfrom(buffer_size)
        # await_ack(server.recvfrom)
        content = output.decode()
        # print(content)
        ip, port = clientaddress[0], clientaddress[1]
        
        # Caso seja um ack
        if "/ACK-" in content or "/NAK-" in content: 
            if checksum_receiver_checker(content, isack=True): print("ack não corrompido no server") 
            else: print("corrompido")
            transmiter_state_machine.await_ack(content, port)
        elif "/PKT-" in content:
            if receiver_state_machine.await_call(content, clientaddress, clients):
                #print("conteúdo do servidor: ", content)
                print("conteudo antes de checar checksum: ", content)
                if checksum_receiver_checker(content, isack=False):
                    print("pkt não corrompido no server")
                else:
                    print("corrompido")
                # Caso seja um pkt
                
                if "saiu da sessão" in content:
                    clients.remove(clientaddress)
                    
                elif "entrou" in content:
                    clients.append(clientaddress)
                else:
                    content = content.replace("/START/", f"{ip}:{port}/~") 
                
                with open("receive.txt", mode="a", encoding='utf-8') as filea:
                    #print(content)
                    content = content.replace("/START/", f"{ip}:{port}/~")
                    content = content.replace("/END/", f" {datetime.now()} /END/")
                    content = content.replace("/PKT-0/", "")
                    content = content.replace("/PKT-1/", "")

                    # Conteúdo sem checksum
                    content = content.split('/END/')[0] + '/END/'
                    filea.write(content)
                
                if "/END/" in content:
                    transmiter_state_machine.await_call(clientaddress, clients)
                    print()
                    os.remove("receive.txt")
            else:
                print("SEI NAOOO, APAGAR DEPOIS ISSOOOOOOOOOOOOOOOOOOOOOOOOOO")
        
    # except Exception as e:
    #     print(f"Error: {e}")

while True:
    receive_content()
