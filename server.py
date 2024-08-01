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
server.bind(("127.0.0.1", serverport))

# Armazenar quem está conectado na sessão (pensar um pouco melhor sobre o primeiro dict e essa lista)
clients = []

print(f"Servidor iniciado com sucesso às {datetime.now()}")

transmiter_state_machine = TransmiterStateMachine(server, "server")
receiver_state_machine = ReceiverStateMachine(server)

def receive_content():
    try:
        output, clientaddress = server.recvfrom(buffer_size)
        content = output.decode()
        ip, port = clientaddress[0], clientaddress[1]
        
        if "/ACK-" in content: 
            transmiter_state_machine.await_ack(content, clientaddress)
        elif "/PKT-" in content:
            if receiver_state_machine.await_call(content, clientaddress):            
                if "saiu da sessão" in content:
                    clients.remove(clientaddress)
                    
                elif "entrou" in content:
                    clients.append(clientaddress)
                else:
                    content = content.replace("/START/", f"{ip}:{port}/~") 
            
                with open(f"chat/receive-{port}.txt", mode="a", encoding='utf-8') as filea:
                    print(content)
                    content = content.replace("/START/", f"{ip}:{port}/~")
                    content = content.replace("/END/", f" {datetime.now()} /END/")
                    content = content.replace("/PKT-0/", "")
                    content = content.replace("/PKT-1/", "")

                    # Conteúdo sem checksum (em tese)
                    content = content.split('/CRC-')[0]
                    
                    filea.write(content)
                
                if "/END/" in content:
                    transmiter_state_machine.await_call(clientaddress, f"chat/receive-{port}.txt", clients)
                    print()
                    os.remove(f"chat/receive-{port}.txt")
            # else:
            #     print("[PRINT-DEBBUGGER] Pacote corrompido")
        
    except Exception as e:
        print(f"Error: {e}")

while True:
    receive_content()
