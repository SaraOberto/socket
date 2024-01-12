import json
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    primoNumero = float(input("Inserisci il primo numero"))
    operazione = input("Inserisci l'operazione (+,-,*,/,%)")
    secondoNumero = float(input("Inserisci il secondo numero"))
    messaggio ={'primoNumero': primoNumero,
                'operazione': operazione,
                'secondoNumero': secondoNumero}
    messaggio = json.dumps(messaggio) #Trasformiamo l'oggetto in una stringa
    s.sendto(messaggio.encode("UTF-8"),(SERVER_IP, SERVER_PORT))

    data = s.recv(BUFFER_SIZE)
    print("Risultato : ",data.decode())
    continua = input("Vuoi fare un'altra operazione?(s,n)")
    if continua == "n":
        break

s.close()