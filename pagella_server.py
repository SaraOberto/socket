import socket, json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 2048

diz = {'Antonio Barbera': [['Matematica', 8, 1],
                           ['Italiano', 6, 1],
                           ['Inglese', 9.5, 0],
                           ['Storia', 8, 2],
                           ['Geografia', 8, 1]],
       'Giuseppe Gullo': [['Matematica', 9, 0],
                          ['Italiano', 7, 3],
                          ['Inglese', 7.5, 4],
                          ['Storia', 7.5, 4],
                          ['Geografia', 5, 7]],
       'Nicola Spina': [['Matematica', 7.5, 2],
                        ['Italiano', 6, 2],
                        ['Inglese', 4, 3],
                        ['Storia', 8.5, 2],
                        ['Geografia', 8, 2]]
       }

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((SERVER_ADDRESS,SERVER_PORT))
    sock.listen()
    print(f"Server in ascolto su {SERVER_ADDRESS}:{SERVER_PORT}...")
    while True:
        sock_service, address_client = sock.accept()
        with sock_service as sock_client:
            while True:
                messaggio = sock_client.recv(BUFFER_SIZE).decode()
                if not messaggio:
                    break
                messaggio = json.loads(messaggio)
                
                istruzione = (messaggio["istruzione"]).split("#")[1]
                parametri = (messaggio["parametri"])

                parametri = (messaggio["parametri"]).split("/")
                print(parametri)
                
                if istruzione == "list":
                    risp = "OK"
                    risultato = diz
                
                elif istruzione == "get":
                    studente = parametri[1]  
                    if studente in diz:
                        risp = "OK"
                        risultato = diz[studente]
                    else:
                        risp = "KO"
                        risultato = "lo studente non esiste, aggiungilo!!"

                elif istruzione == "set":
                    studente = parametri[1]  
                    print("Parametri:", studente)

                    if studente not in diz:
                        diz[studente] = {}
                        risp = "OK"
                        risultato = "studente aggiunto nel dizionario"
                    else:
                        risp = "KO"
                        risultato = "studente già presente nel dizionario"

                    print("dizionario aggiornato:", diz)

                elif istruzione == "put":
                    studente = parametri[1]
                    materia = parametri[2]
                    voti = parametri[3]
                    ore = parametri[4]
                    print(studente,materia,voti,ore)                
                    if studente in diz:
                        diz[studente] = [materia,voti,ore]
                        risp = "OK"
                        risultato = "voti aggiunti"
                    else:
                        risp = "KO"
                        risultato = "lo studente non è presente nel dizionario, aggiungilo!!"   
                    print(risp)
                    print(risultato)
                    
                dati = {"risposta":risp,
                        "valori":risultato,
                }                   
                sock_service.sendall((json.dumps(dati).encode()))



