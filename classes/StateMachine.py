import time
import threading
from socket import *
from packages_functions import checksum_calculator, checksum_receiver_checker

sequences = {}
timers = {}
indexes = {}

class TransmiterStateMachine:
    def __init__(self, socket: socket, user_type):
        self.socket = socket
        
        self.packages = []
        self.user_type = user_type
        
        self.time_limit = 0.03

    def make_packages(self, file_text ):     
        self.packages = []          
        with open(file_text, mode="rb") as file1:
            while True:
                data = file1.read(500)
                
                if not data: break

                formated_content = checksum_calculator(data, 16)
                self.packages.append(formated_content)

    def timer_receive_ack(self, address):
        repeat_times = 10
        interval = self.time_limit / repeat_times
        
        if address not in list(timers.keys()):
            timers[address] = {
                "ack": False,
                "exploded": False
                }

        for _ in range(3):
            timers[address]["ack"] = False
            timers[address]["exploded"] = False

            self.send_package(address, indexes[address[1]])
            
            for _ in range(repeat_times):
                time.sleep(interval)
                
                if timers[address]["ack"]:
                    timers[address]["exploded"] = False
                    break
                
            if not timers[address]["ack"]:
                print("ai papai, macetei")
                timers[address]["exploded"] = True
            else:
                break
    
    def send_package(self, address, index):
        print(f"ENVIOU PKT-{sequences[address[1]]} e o PACKAGE é {index}", address[1])
        package: bytes = self.packages[index]
        
        package = f"{package.decode()}/PKT-{sequences[address[1]]}/".encode()
        
        self.socket.sendto(package, address)
    
    def await_call(self, address, file_text, clients = []):
        if address[1] not in list(sequences.keys()):
            sequences[address[1]] = 0
            
        self.make_packages(file_text)
        
        for client in clients:
            indexes[client[1]] = 0
            if client != address or self.user_type == "client":
                threading.Thread(target=self.timer_receive_ack, args=(client,)).start()

    def await_ack(self, content, address):
        received_sequence = int(content.split("/ACK-")[1][0])
        port = address[1]
        
        current_sequence = sequences[port]
        
        print(f"[PRINT-DEBBUGGER] CHEGOU ACK-{received_sequence}", port)
        
        if received_sequence != current_sequence or not checksum_receiver_checker(content, isack=True):
            print("[PRINT-DEBBUGGER] Está corrompido ou é um ACK diferente")
            pass
        elif timers[address]["exploded"]:
            print("[PRINT-DEBBUGGER] Timer estouro")
            pass
        else:
            timers[address]["ack"] = True
            timers[address]["exploded"] = False
            indexes[address[1]] += 1
            
            sequences[port] = 0 if current_sequence == 1 else 1
            
            if indexes[address[1]] < len(self.packages):
                threading.Thread(target=self.timer_receive_ack, args=(address,)).start()

class ReceiverStateMachine:
    def __init__(self, socket: socket):
        self.socket = socket
        
    def await_call(self, content, address):
        port = address[1]
        
        if port not in list(sequences.keys()):
            sequences[port] = 0  
            
        received_sequence = int(content.split("/PKT-")[1][0])
        current_sequence = sequences[port]
        
        print(f"[PRINT-DEBBUGGER] CHEGOU PKT-{received_sequence}/ ", port)

        # (Vitor) - Colocar apenas 1 encode, tem um dentro do checksum
        data = f"/ACK-{received_sequence}/".encode()
        
        # Adicionando o checksum no ack
        formated_content = checksum_calculator(data, 16)
        print(f"[PRINT-DEBBUGGER] Conteudo com checksum - {formated_content}")
        
        self.socket.sendto(formated_content, address)
        print(f"[PRINT-DEBBUGGER] ENVIOU ACK-{received_sequence}", port)

        if received_sequence == current_sequence:
            sequences[port] = 0 if current_sequence == 1 else 1
            return True

        return False
        