# Projeto de Redes - Comunicação UDP 

Repositório criado destinado para o projeto da disciplina "IF975-Redes de Computadores" como forma de avaliação. O projeto foi dividido em duas etapas, sendo a primeira responsável por criar uma comunicação utilizando o protocolo da camada de transporte UDP e a segunda etapa implementar um sistema de transferência de mensagens confiável, o RDT 3.0. 

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

## Primeira Etapa

A primeira etapa foi responsável por implementar uma simples aplicação de "chat" entre usuários por meio do auxílio de um "servidor" por meio da transmissão de pacotes utilizando o protocolo da camada de transporte UDP, conhecido pela não confiabilidade de envio de pacotes.

## Segunda Etapa

A segunda etapa do projeto veio como um complemento da estrutura criada anteriormente, pois, como comentado anteriormente, há a presença de uma insegurança por parte dos envios dos pacotes com a possível corrupção dos mesmos. Para sanar essa situação, o RDT 3.0 foi implementado, adicionando o funcionamento de transmissor e receptor com o recebimento de ACK e utilização de "Sequence Number", além da adição do checksum.

## Desenvolvimento do projeto: 

O desenvolvimento do projeto foi organizado em divisão de tarefas, de forma adequada e compatível com as habilidades de cada integrante. Com o andamento da construção do programa, buscamos estabelecer uma linha direta de comunicação para a cooperação nas tarefas estabelecidas para ambos, fator que permitiu a correção de problemas e sugestões para a melhoria do projeto. Durante o desenvolvimento, utilizamos a principal ferramenta de controle de versões de software, que seria o GitHub, permitindo que as versões criadas fossem registradas e facilitava a visualização.

## Ferramentas, Bibliotecas e Frameworks utilizados: 

Utilizamos diversas bibliotecas nativas do próprio Python para a construção do projeto. O "socket" foi a lib vital para o funcionamento adeqaudo do projeto, havendo o uso de bibliotecas auxiliares para algumas questões, como time/datetime (auxiliar o funcionamento do timer no RDT 3.0) e threading (para garantir um funcionamento adequado de recebimento e envio de mensagens por parte do cliente). 
