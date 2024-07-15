import math

def send_for_clients(type_user, clients, adress, sendto, data):
    if type_user == "server":
        for client in clients:
            if adress != client:
                sendto(data, client)
    else:
        sendto(data, adress)

def checksum_sender_calculator(content, block_length):
    # Processo de divisão em blocos do pacote
    number_blocks = math.ceil(len(content)/block_length)
    start = 0
    end = block_length
    checksum_value = 0
    for _ in range(number_blocks): 
        checksum_segment = content[start:end]
        for byte_value in checksum_segment:
            checksum_value += byte_value
        start = end
        end += block_length

    return bin(checksum_value)


def send_packages(content, sendto, type_user, filetxt, adress, clients = []):
    if type_user == "client":
        with open(filetxt, mode="w", encoding='utf-8') as file4:
            file4.write(content)
            
    with open(filetxt, mode="rb") as file1:
        while True:
            # Monta pacote
            data = file1.read(500)
            checksum = checksum_sender_calculator(data, 16)
            print(len(data), checksum)
            #print(len(data))
            if not data: break
            # Envia
            send_for_clients(type_user, clients, adress, sendto, data)
            
            # Await_acl
            
            
            
            # data = f"/ACK-{sequence}/ {data}"
            
            
    

    
            