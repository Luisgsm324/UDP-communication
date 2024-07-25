import time
from socket import *
from packages_functions import send_packages


class StateMachine:
    def __init__(self):
        self.sequence = 0
        self.state = f"Await call {self.sequence}"
        
        self.state_timer = "Stopped"
        self.packages = []

    def run_timer(self):
        current_time_timer = 0
        limit_time_timer = 2

        
        while current_time_timer <= limit_time_timer:
            time.sleep(1)
            current_time_timer += 1
        
        # analisa melhor (eu acho) se o tempo atual do timer atingiu o limite
        # logo se o tempo limite é atingido, o timer explode (dando timeout) ou o timer é parado
        if current_time_timer == limit_time_timer: 
            self.state_timer = "Boom"

        else: 
            self.state_timer = "Stopped"


    def await_call(self, content, sendto, type_user, filetxt, adress, clients = []):
        # vai continuar enviando os pacotes utilizando a função send_packages
        send_packages(content, sendto, type_user, filetxt, adress, clients)
        # agora atualiza o estado da máquina para "Await ACK" (aguardando ACK) com o número de sequência atual
        self.state = f"Await ACK {self.sequence}"
        # depois inicia o timer para controlar o tempo de espera pelo ACK e chama a função para aguardar receber o ACK
        self.run_timer()
        self.await_ack(sendto, adress)

        # recebeu ordem ed enviar
            # montar pacote
            # enviar
            # começar timer 
            # mudar estado para esperar ack

        
    def await_ack(self, server: socket, buffer_size):
        output, clientadress = server.recvfrom(buffer_size)
        content = output.decode() 

        # checa se o conteúdo recebido começa com "/ACK-" e pega o número do ACK recebido
        if content.startswith("/ACK-"):
            ack_received = int(content.split("/ACK-")[1].split("/")[0])

        # e se não for um ACK vai chamar novamente o await_call() para reenviar o pacote
        else: 
            self.await_call()

        # o ACK recebido não corresponde à sequência esperada? não faça nada
        if ack_received != self.sequence: 
            pass

        # se o timer estourar, reenvia o pacote
        if self.state_timer == "Boom":
            self.await_call()

        # agora se o ACK for recebido corretamente ele muda o estado para "Await call"
        else:
            self.state = f"Await call {self.sequence}"
            # logo após alterna a sequência para o próximo valor (0 ou 1)
            self.sequence = (self.sequence + 1) % 2
        



