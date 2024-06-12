"""
lado de quem vai mandar a mensagem

tem um arquivo "mensagem" que muda conforme vc manda
mensagens diferentes.
ele é meio que o campo de texto do whatsapp.
"""

# recebe o texto e o nome pra o arquivo
# esse arquivo vai ser criado dentro da função

def string_para_txt(conteudo, nome_arquivo):

  with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)

# recebe um nome de arquivo e retorna em pacotes ou pacote único

def fragmentar_arquivo(nome_arquivo, tamanho_buffer=1024):
  pacotes = []

  with open(nome_arquivo, 'rb') as arquivo:
    while True:
      
      dados = arquivo.read(tamanho_buffer)
      if not dados: break

      pacotes.append(dados)

  return pacotes

# recebe string e retorna lista de pacote(s) pronto(s)

def empacotar_string(texto):
  endereco = "../utils/remetente/mensagem.txt"
  string_para_txt(texto, endereco)

  pacotes = fragmentar_arquivo(endereco)
  
  return pacotes
