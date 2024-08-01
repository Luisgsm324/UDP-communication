# Projeto de Redes - Comunicação UDP 

Repositório criado destinado para o projeto da disciplina "IF975-Redes de Computadores" como forma de avaliação. O projeto foi dividido em duas etapas, sendo a primeira responsável por criar uma comunicação utilizando o protocolo da camada de transporte UDP e a segunda etapa implementar um sistema de transferência de mensagens confiável, o RDT 3.0. 

## Segunda Etapa

A segunda etapa foi responsável por ampliar o funcionamento da aplicação de chat entre diversos usuários, entretanto objetivando a implementação de um mecanismo de segurança do envio de mensagens utilizando o protocolo UDP, que seria o RDT 3.0. O RDT 3.0 adota certos funcionamentos específicos não presentes na primeira entrega que engloba a inclusão do checksum (valor para verificação de corrupção do pacote/ack), sequence number (outro valor para verificação de qual pacote está sendo tratado) e do ACK, que serve como uma forma de confirmação do recebimento. A execução do código segue uma ideia semelhante ao da primeira etapa, sem nenhuma diferenciação entre elas.

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

A execução do código não foi alterada, entretanto a estrutura básica do código sofreu significativas modificações entre as entregas. Construímos classes que corresponderiam ao estados da máquina de estados finitas que representa o funcionamento do RDT 3.0, além de alterar quase que por completo o funcionamento da construção de pacotes e envio dos mesmos. Todas essas alterações objetivam implementar adequadamente o serviço de transporte de segurança.