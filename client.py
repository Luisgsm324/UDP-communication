from socket import *
import threading
import time
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
            time.sleep(0.5)
            content = output.decode()
            print(content)
    except:
        pass

# Enviar conteúdo
# Precisa rodar apenas quando vai enviar algum conteúdo
def handle_input_content():
    while True:
        data = input("")
        data = f"{name}: {data}"
        if 'bye' in data: 
            send_content(data)
            print("Você saiu da sessão. Até a próxima :)")
            client.close()
            break
        send_content(data)

def send_content(content):
    try:
        send_packages(content, client.sendto)
    except: 
        print("Error")
        
# Entrar na sessão
def enter_session(name):
    content = f"O usuário {name} entrou na sala"
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
