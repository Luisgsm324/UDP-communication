import math
import hashlib



# verificar se há função mais otimizada para isso
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
        formated_content = content + f'/CRC-{checksum_value}/'.encode()
        print(formated_content)
        return formated_content
    
    return binary_value
        

def checksum_receiver_checker(data, isack=True):
    if isack:
        content, checksum_content = data.split("/CRC-")[0], data.split("/CRC-")[1][0:-1]
    else:
        content, checksum_content = data.split("/CRC-")[0], data.split("/CRC-")[1].split('/')[0]
    print("checksum: ", checksum_content)
    #print(checksum_content, content)
    content = content.encode()
    checksum_value = checksum_calculator(content, 16, type_user='server')

    checksum_result = bin(int(checksum_value, 2) + int(checksum_content, 2))

    # validar certas referências
    ref = ''
    for _ in range(len(checksum_content)): ref += '1' # serve para fazer o valor de referência (tem que dar igual a 1 n vezes, sendo n o tamanho)

    return ref == checksum_result[2:]