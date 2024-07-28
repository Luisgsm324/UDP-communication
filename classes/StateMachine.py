import time, timeit
import threading
from socket import *
from packages_functions import send_packages, send_for_clients


sequences = {}

class TransmiterStateMachine:
    def __init__(self, socket: socket, buffer_size, user_type, file_text):
        self.socket = socket
        self.buffer_size = buffer_size
        
        
        self.packages = []
        self.user_type = user_type
        self.file_text = file_text
        self.time_limit = 0.01 # 10 ms em segundos 
        self.timer_exploded = False # Tempo do timer explodiu
        self.ack_received = False # Recebeu o ACK
    
    def timer_receive_ack(self):
        repeat_times = 10
        print(self.time_limit)
        for _ in range(repeat_times):
            time.sleep(self.time_limit/repeat_times)
            if self.ack_received:
                print("não explodiu")
                self.timer_exploded = False
                break
        if not self.ack_received:
            print("explodiu")
            self.timer_exploded = True

    def await_call(self, address, clients = []):
        for _ in range(3):
            self.address = address
            self.clients = clients
            
            if address[1] not in list(sequences.keys()):
                sequences[address[1]] = 0     
            
            if self.user_type == "client":
                with open(self.file_text, mode="a", encoding="utf-8") as file:
                    file.write(f"/PKT-{sequences[address[1]]}/")

            self.packages = send_packages(self.socket.sendto, self.user_type, self.file_text, address, clients, sequences)
            self.ack_received = False
            self.timer_exploded = False
            
            timer_ack_function = threading.Thread(target=self.timer_receive_ack)
            timer_ack_function = timer_ack_function.start()
            #time.sleep(self.time_limit) 
            if not self.timer_exploded:
                break
        # Iniciar timer
        

        # print(f"ENVIOU PKT-{sequences[address[1]] if address[1] in sequences else 0}", address[1])
        # self.run_timer()

        # recebeu ordem ed enviar
            # montar pacote
            # enviar
            # começar timer 
            # mudar estado para esperar ack

    # def resend_packages(self):
    #     for package in self.packages:
    #         if self.user_type == "server":
    #             send_for_clients(self.user_type, self.clients, self.address, self.socket.sendto, package)
    #         else:
    #             self.socket.sendto(package, self.address)
        
    def await_ack(self, content, port, nak=False):
        received_sequence = int(content.split("/ACK-")[1][0])
        
        current_sequence = sequences[port]
        
        self.ack_received = True
        # Testar isso aq
        print(f"CHEGOU ACK-{received_sequence}", port , content, sequences)
        
        if received_sequence != current_sequence or nak:
            # esperar um timer estourar
            print("Esta corrompido ou é um ack diferente")
            for package in self.packages:
                self.socket.sendto(package, self.address)
            pass
        
        else:
            sequences[port] = 0 if current_sequence == 1 else 1 

            # Parar o timer
            
        # Se recebeu, mas está corrompido ou é um ack diferente do sequence
            # espera o timer estorar
        
        # Se o timer estourar
            # reenvia os ppacotes
            # inicia o timer

        # Se recebeu, nao está corrompido e é um ack esperarado
            # para o timer
            # muda o estado para esperar chamda
            # muda sequenec para 1
            
class ReceiverStateMachine:
    def __init__(self, socket: socket, buffer_size, user_type, file_text):
        self.socket = socket
        self.buffer_size = buffer_size
        
        self.packages = []
        self.user_type = user_type
        self.file_text = file_text
    
    
    def await_call(self, content, address, clients=[]):
        port = address[1]
        if port not in list(sequences.keys()):
            sequences[port] = 0  
            
        self.address = address
        self.clients = clients
        
        # nao corrompido e 
        received_sequence = int(content.split("/PKT-")[1][0])
        print(f"CHEGOU PKT-{received_sequence}/ ", port, content)
        current_sequence = sequences[port]
        
        data = f"/ACK-{received_sequence}/".encode()
        
        self.socket.sendto(data, address)
        
        if received_sequence == current_sequence:
            print(f"ENVIOU ACK-{received_sequence}", port, content)
            sequences[port] = 0 if current_sequence == 1 else 1
            return True
        else:
            print("ERROU EM")
        return False
    
        
        