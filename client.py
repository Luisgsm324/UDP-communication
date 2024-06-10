from socket import *
import threading
import time
import sys

SERVERNAME = 'localhost'
SERVERPORT = 5000
BUFFER_SIZE = 1024 # Tamanho do buffer especificado pelos requisitos do projeto
# Socket do client
# AF_INET -> USANDO IPV4
# SOCK_DGRAM -> PROTOCOLO UDP
client = socket(AF_INET, SOCK_DGRAM)
queue_content = []

def check_content():
    if len(queue_content) != 0:
        print(queue_content[0])
        queue_content.pop(0)

# Receber conteúdo
# Precisa rodar o tempo todo (pode receber mensagem a qualquer momento)
def receive_content():
    output, serveradress = client.recvfrom(BUFFER_SIZE)
    time.sleep(0.5)
    content = output.decode()
    queue_content.append(content)
    check_content()

# Enviar conteúdo
# Precisa rodar apenas quando vai enviar algum conteúdo
def send_content(content):
    # True -> Deu certo // False -> Deu errado :(
    try:
        client.sendto(content.encode(), (SERVERNAME, SERVERPORT))
    except:
        print("Error")

# Entrar na sessão
def enter_session(name):
    content = f"O usuário {name} entrou na sala"
    send_content(content)   

def main():   
    name = input("Insira o seu nome: ")
    enter_session(name)
    
    while True:
        # uma threading que vai estar sempre rodando recebendo o conteúdo
        threading.Thread(target=receive_content).start()
        time.sleep(1)
        data = input("")
        data = f"{name}: {data}"     
        # Basicamente, vamos pegar a informação que está em STR e converter para Byte, em seguida colocamos uma tupla que tem o nome do servidor destino e a porta
        send_content(data)
        
        if 'bye' in data: 
            sys.exit()           
            break

    client.close()

main()