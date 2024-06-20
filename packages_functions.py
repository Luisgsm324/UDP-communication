# ------------------------ Funções para enviar o conteúdo -----------------------------------------
endereco = "message.txt"
from constants import *

# tem que fazer a divisao por pacotes aqui, talkei?
def send_packages(content, sendto, type_user, filetxt, adress, clients = []):
  with open(filetxt, mode="w", encoding='utf-8') as file:
      file.write(content)
      
  with open(filetxt, mode="rb") as file:
      for data in file.readlines():
          if type_user == "server":
             for client in clients:
                  if adress != client:
                    sendto(data, client)
          else:
              sendto(data, adress)

            
  
  

# ------------------------ Funções para receber o conteúdo -----------------------------------------

# def txt_para_string(nome_arquivo = "unknown.txt"):

#   with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
#     conteudo = arquivo.read()

#   return conteudo

# # recebe pacotes e monta em um arquivo só

# def remontar_arquivo(pacotes, nome_arquivo_saida = "unknown.txt"):

#   print(pacotes)
#   with open("message.txt", 'wb') as arquivo_saida:
#     for pacote in pacotes:
#       arquivo_saida.write(pacote)
  
#   return nome_arquivo_saida

# # recebe pacotes e devolve a string lida do arquivo recebido
# def desempacotar_string(pacotes):
#   # remetente +=".txt"
#   endereco = "message.txt"
#   print(pacotes, "pacotes")
#   return txt_para_string(remontar_arquivo(pacotes, endereco))