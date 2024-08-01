# Projeto de Redes - Comunicação UDP 

Repositório criado destinado para o projeto da disciplina "IF975-Redes de Computadores" como forma de avaliação. O projeto foi dividido em duas etapas, sendo a primeira responsável por criar uma comunicação utilizando o protocolo da camada de transporte UDP e a segunda etapa implementar um sistema de transferência de mensagens confiável, o RDT 3.0. 

## Primeira Etapa

A primeira etapa foi responsável por implementar uma simples aplicação de "chat" entre usuários por meio do auxílio de um "servidor" por meio da transmissão de pacotes utilizando o protocolo da camada de transporte UDP, conhecido pela não confiabilidade de envio de pacotes. O programa utiliza da estrutura fornecida pela biblioteca socket para fornecer o necessário para realizar essa transmissão e o processo de comunicação tem a necessidade de "rodar" o código como cliente e servidor, assim como outros clientes para efetuar a comunicação entre diversos usuários.

## Execução

Para a execução do código, é necessário:

1. Ter o python instalado em sua máquina

2. Escolher o lado que deseja executar o código, cliente ou servidor.

### Execução servidor

3. Iniciar o projeto

(Windows)

```bash
python server.py
```

***

(Mac/Linux)

```bash
python3 server.py
```

### Execução cliente

3. Iniciar o projeto

(Windows)

```bash
python client.py
```

***

(Mac/Linux)

```bash
python3 client.py
```

## Integrantes do projeto:

[Luís Moreira (lfsgm)](https://github.com/Luisgsm324) 

[Vitor Mendonça (vhmq)](https://github.com/VitorMendonca62) 


## Observações necessárias 

Devido à necessidade da fragmentação em pacotes, o sistema utiliza de um mecanismo com o sufixo '/END/' para a identificação de que se trata do último pacote relacionado à mensagem enviada por um usuário. A identificação desse sufixo é realizada em ambos os lados, tanto o servidor como o cliente.
