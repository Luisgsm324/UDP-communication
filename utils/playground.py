from remetente.enviar import empacotar_string
from receptor.receber import desempacotar_string

# aqui pra testar
usuario = "Pedrinho carlos"
mensagem = "Olá, pessoas. Estou mandando mais uma mensagem que agora é diferente."

# primeiro o sujeito envia a mensagem
recebido = empacotar_string(mensagem)

# aí o servidor vai receber a mensagem dele
print(desempacotar_string(recebido, usuario))