import os

def send_packages(content, sendto, type_user, filetxt, adress, clients = []):
    if type_user == "client":
        with open(filetxt, mode="w", encoding='utf-8') as file4:
            file4.write(content)
            
    with open(filetxt, mode="rb") as file1:
        while True:
            data = file1.read(255)
            
            if not data: break

            if type_user == "server":
                for client in clients:
                    if adress != client:
                        sendto(data, client)
            else:
                sendto(data, adress)
    

    
            