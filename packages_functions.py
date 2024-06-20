# ------------------------ Funções para enviar o conteúdo -----------------------------------------
endereco = "message.txt"
from constants import *

# recebe um nome de arquivo e retorna em pacotes ou pacote único

# def fragmentar_arquivo(nome_arquivo, package_size=20):
#   pacotes = []

#   with open(nome_arquivo, 'rb') as arquivo:
#     while True:
      
#       dados = arquivo.read(package_size)
#       if not dados: break

#       pacotes.append(dados)

#   return pacotes

# # recebe string e retorna lista de pacote(s) pronto(s)

# def empacotar_string(fileo):

#   with open(endereco, 'w', encoding='utf-8') as arquivo:
#     arquivo.write(conteudo)

#   pacotes = fragmentar_arquivo(endereco)
  
#   return pacotes

def send_packages(content, sendto, package_size=255):
  with open("message.txt", mode="w", encoding='utf-8') as file:
      file.write(content)
      
  with open("message.txt", mode="rb") as file:
      data = b""
      while not data.decode().endswith("/END/"):
          data = file.read(package_size)
          if not data: data = "/END/".encode()

          sendto(data, (SERVERNAME, SERVERPORT))
          
# ------------------------ Funções para receber o conteúdo -----------------------------------------

def txt_para_string(nome_arquivo = "unknown.txt"):

  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

  return conteudo

# recebe pacotes e monta em um arquivo só

def remontar_arquivo(pacotes, nome_arquivo_saida = "unknown.txt"):

  print(pacotes)
  with open("message.txt", 'wb') as arquivo_saida:
    for pacote in pacotes:
      arquivo_saida.write(pacote)
  
  return nome_arquivo_saida

# recebe pacotes e devolve a string lida do arquivo recebido
def desempacotar_string(pacotes):
  # remetente +=".txt"
  endereco = "message.txt"
  print(pacotes, "pacotes")
  return txt_para_string(remontar_arquivo(pacotes, endereco))