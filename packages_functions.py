
def send_for_clients(type_user, clients, adress, sendto, data):
    if type_user == "server":
        for client in clients:
            if adress != client:
                sendto(data, client)
    else:
        sendto(data, adress)

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
            send_for_clients(type_user, clients, adress, sendto, data)
            
            # Await_acl
            
            
            
            # data = f"/ACK-{sequence}/ {data}"
            
            
    

    
            