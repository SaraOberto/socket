import json
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()

    while True:
        print("Server in attesa di una connesione...")
        sock_service, address_client = sock_server.accept()
        print(f"Ricevuta connessione da {address_client}")
        with sock_service as sock_client:
            while True:
                dati = sock_client.recv(BUFFER_SIZE).decode()  
                if not dati:
                    break          
                dati=json.loads(dati)
                primoNumero = dati['primoNumero']
                operazione = dati['operazione']
                secondoNumero = dati['secondoNumero']

                risultato = 0
                if operazione == "+":
                    risultato = primoNumero + secondoNumero
                elif operazione == "-":
                    risultato = primoNumero - secondoNumero
                elif operazione == "*":
                    risultato = primoNumero * secondoNumero
                elif operazione == "/":
                    if secondoNumero !=0:
                        risultato = primoNumero + secondoNumero
                    else:
                        risultato = "Impossibile"
                elif operazione == "%":
                    risultato = primoNumero % secondoNumero
                
                risultato=str(risultato)
                print(risultato,type(risultato))
                sock_client.sendall(risultato.encode())
