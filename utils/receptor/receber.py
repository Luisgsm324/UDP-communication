"""
lado de quem vai receber a mensagem

na pasta "mensagens" tem as mensagens dos diferentes
usuários que mandaram.
"""

# recebe o nome ou endereço relativo pra poder achar o arquivo
# retorna uma string que é o que tava dentro do arquivo

def txt_para_string(nome_arquivo = "unknown.txt"):

  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

  return conteudo

# recebe pacotes e monta em um arquivo só

def remontar_arquivo(pacotes, nome_arquivo_saida = "unknown.txt"):

  with open(nome_arquivo_saida, 'wb') as arquivo_saida:
    for pacote in pacotes:
      arquivo_saida.write(pacote)
  
  return nome_arquivo_saida

# recebe pacotes e devolve a string lida do arquivo recebido

def desempacotar_string(pacotes, remetente = "unknown"):
  # remetente +=".txt"
  endereco = "../utils/receptor/mensagens/" + remetente + ".txt"
  return txt_para_string(remontar_arquivo(pacotes, endereco))