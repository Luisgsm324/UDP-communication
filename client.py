from socket import *
import threading
import time
import os
from datetime import datetime
from packages_functions import *

SERVERNAME = 'localhost'
SERVERPORT = 5000
BUFFER_SIZE = 1024 # Tamanho do buffer especificado pelos requisitos do projeto
# Socket do client
# AF_INET -> USANDO IPV4
# SOCK_DGRAM -> PROTOCOLO UDP
client = socket(AF_INET, SOCK_DGRAM)
# Receber conteúdo
# Precisa rodar o tempo todo (pode receber mensagem a qualquer momento)

def receive_content():
    try:
        while True:
            output, serveradress = client.recvfrom(BUFFER_SIZE)
            content = output.decode()
            
            if "/END/" not in content:
                with open("message.txt", mode="a", encoding='utf-8') as file_append_1:
                    file_append_1.write(content)
            else:
                with open("message.txt", mode="rb") as file_read_1:
                    data = file_read_1.read().decode() 
                
                    if len(data) > 250:
                        data = f"{data.split("/END/")[1]}{content}"
                    else: 
                        data = content
                    
                    print(data.replace("/END/", f" {datetime.now()}"))
        
                os.remove("message.txt")                
    except:
        pass

# Enviar conteúdo
# Precisa rodar apenas quando vai enviar algum conteúdo
def handle_input_content():
    while True:
        data = input("")
        if 'bye' in data: 
            data = f"O usuário {name} saiu da sessão às /END/"
            send_content(data)
            print("Você saiu da sessão. Até a próxima :)")
            client.close()
            break
        else:
            data = f"/START/{name}: {data}/END/"
            send_content(data)
            

def send_content(content):
    try:
        send_packages(content, client.sendto, "client", "message.txt", (SERVERNAME, SERVERPORT))
    except: 
        print("Error")
        
# Entrar na sessão
def enter_session(name):
    content = f"O usuário {name} entrou na sala às /END/"
    send_content(content)

def main():
    global name
    name = input("Insira o seu nome: ")
    enter_session(name)

    thread_receive = threading.Thread(target=receive_content)
    thread_receive.start()
    thread_send = threading.Thread(target=handle_input_content)
    thread_send.start()

main()
