import time
from socket import *



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
        
        if current_time_timer == 11: self.state_timer = "Boom"
        else: self.state_timer = "Stopped"


    def await_call(self, content, sendto, type_user, filetxt, adress, clients = []):
        send_packages(content, sendto, type_user, filetxt, adress, clients = [])
        self.state = f"Await ACK {self.sequence}"
        self.run_timer()
        self.await_ack(self,)

        # recebeu ordem ed enviar
            # montar pacote
            # enviar
            # começar timer 
            # mudar estado para esperar ack

        
    def await_ack(self, server: socket, buffer_size):
        output, clientadress = server.recvfrom(buffer_size)
        content = output.decode() 

        if content.startswith("/ACK-"): ack_received = int(content[5])
        else: self.await_call()


        if ack_received != self.sequence: pass

        if 
        # Se recebeu, mas está corrompido e é um ack diferente do sequence
            # espera o timer estorar
        
        # Se o timer estourar
            # reenvia os ppacotes
            # inicia o timer

        # Se recebeu, nao está corrompido e é um ack esperarado
            # para o timer
            # muda o estado para esperar chamda
            # muda sequenec para 1
        



