from socket import *
import threading
import time
import os
from datetime import datetime
from packages_functions import *
from random import randint
from classes.StateMachine import *

SERVERNAME = 'localhost'
SERVERPORT = 5000
BUFFER_SIZE = 1024 # Tamanho do buffer especificado pelos requisitos do projeto
# Socket do client
# AF_INET -> USANDO IPV4
# SOCK_DGRAM -> PROTOCOLO UDP
client = socket(AF_INET, SOCK_DGRAM)
port = randint(1000,9999)
client.bind(("localhost", port))
# Receber conteúdo
# Precisa rodar o tempo todo (pode receber mensagem a qualquer momento)

transmiter_state_machine = TransmiterStateMachine(client, BUFFER_SIZE, "client", f"message-{port}.txt")
receiver_state_machine = ReceiverStateMachine(client, BUFFER_SIZE, "client", f"message-{port}.txt")

def write_txt(content, mode="w"):
    with open(f"message-{port}.txt", mode=mode, encoding='utf-8') as file:
        file.write(content)

def receive_content():
    # try:
        while True:
            output, serveraddress = client.recvfrom(BUFFER_SIZE)
            content = output.decode()
            # condition = receiver_checksum_function(content)
            # print(condition, 'Client')

            if "/PKT-" in content:
                if receiver_state_machine.await_call(content, serveraddress):
                    write_txt(content, "a")
                
                    if "/END/" in content:
                        with open(f"message-{port}.txt", mode="rb") as file_read_1:
                            data = file_read_1.read().decode()
                            data = data.replace("/END/", "")
                            
                            if "/START/" in data:
                                print(content)
                            else:
                                print(data) 
                                
                        os.remove(f"message-{port}.txt")
                else:
                    print("TA ERRADO AQUI Ó")
            elif "/ACK-" in content or "/NAK-" in content:
                transmiter_state_machine.await_ack(content, serveraddress[1], "/NAK-" in content)
            else:
                print("EROUUUUUU")
    # except: 
    #     print("ERRO AQUi")
# Enviar conteúdo
def handle_input_content():
    connected = False
    while True:
        data = input("")
        if connected:
            if 'bye' in data: 
                data = f"O usuário {name} saiu da sessão às /END/"
                send_content(data)
                print("Você saiu da sessão. Até a próxima :)")
                client.close()
                os.remove(f"message-{port}.txt")
                break
            
            else:
                data = f"/START/{name}: {data}/END/"
                send_content(data)
        else:
            if data.startswith('hi, meu nome eh '):
                name = data.split("eh ")[1]
                connected = True
                enter_session(name)
            else:
                print("Você não está conectado em nenhuma sessão.")

def send_content(content):
    # try:
        write_txt(content, "w")
        transmiter_state_machine.await_call((SERVERNAME, SERVERPORT))
        write_txt("", "w")

    # except: 
    #     print("Error")
        
# Entrar na sessão
def enter_session(name):
    content = f"O usuário {name} entrou na sala às /END/"
    send_content(content)

def main():
    thread_receive = threading.Thread(target=receive_content)
    thread_receive = thread_receive.start()
    thread_send = threading.Thread(target=handle_input_content)
    thread_send.start()

main()
