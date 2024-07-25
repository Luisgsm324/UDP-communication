import math

def send_for_clients(type_user, clients, adress, sendto, data):
    if type_user == "server":
        for client in clients:
            if adress != client:
                sendto(data, client)
    else:
        sendto(data, adress)

# verificar se há função mais otimizada para isso
def one_complement(value):
    result = ''
    for number in value:
        if number == '1':
            result += '0'
        else: result += '1'
    return result

def checksum_calculator(content, block_length, type_user='client'):
    # Processo de divisão em blocos do pacote
    #print(content)
    number_blocks = math.ceil(len(content)/block_length)
    start = 0
    end = block_length
    checksum_value = 0
    for _ in range(number_blocks): 
        checksum_segment = content[start:end]
        #print(checksum_segment)
        for byte_value in checksum_segment:
            checksum_value += byte_value
        start = end
        end += block_length
    
    binary_value = bin(checksum_value)[2:] # Os dois primeiros números servem para falar que o número é binário (o 0b)
    if type_user == 'client':
        checksum_value = one_complement(binary_value)
        formated_content = content + checksum_value.encode()
        return formated_content
    
    return binary_value
        

def checksum_receiver_checker(data):
    content, checksum_content = (data.split('/END/')[0] + '/END/').encode(), data.split('/END/')[1]
    checksum_value = checksum_calculator(content, 16, type_user='server')

    checksum_result = bin(int(checksum_value, 2) + int(checksum_content, 2))
    
    # validar certas referências
    ref = ''
    for _ in range(len(checksum_content)): ref += '1' # serve para fazer o valor de referência (tem que dar igual a 1 n vezes, sendo n o tamanho)

    if ref == checksum_result[2:]:
        print("Bateu, amigão!")
        # agora obtém também o número de sequência
        seq_num = int(data.split("/START-")[1].split("/")[0])

    else:
        print("não bateu")
        seq_num = -1
    
    return content.decode(), seq_num

def send_packages(content, sendto, type_user, filetxt, adress, clients = []):
    if type_user == "client":
        with open(filetxt, mode="w", encoding='utf-8') as file4:
            file4.write(content)
            
    with open(filetxt, mode="rb") as file1:
        while True:
            # Monta pacote
            data = file1.read(500)
            
            if not data: break
            # Envia
            
            formated_content = checksum_calculator(data, 16)
            #new_content = sender_checksum_function(data)

            send_for_clients(type_user, clients, adress, sendto, formated_content)
            
            # Await_acl
            
            
            
            # data = f"/ACK-{sequence}/ {data}"
            
            
    # /START/luis: olaaa/END/

#100011110011101    

#000110101101