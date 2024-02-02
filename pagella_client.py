import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 2048


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_IP,SERVER_PORT)) 
    print('comandi che puoi usare: \n #list (vedere voti inseriti) \n #get /nomestudente (richiedere voti di uno studente) \n #set /nomestudente (aggiungere uno studente) \n #put /nomestudente/materia/voto/ore (aggiungere voti alla materia di uno studente) \n #close (concludere la connessione)')

    while True:
            
        istruzione = (input("Inserisci istruzione (prima del istruzione inserire #): "))
        if (istruzione != "#list" and istruzione != "#close"):
            if(istruzione == "#put"):
                parametri = (input("Inserisci /studente/materia/voto/ore : "))
            else:
                parametri = (input("Inserisci studente (prima dello studente inserire /): "))
        elif(istruzione == "#close"):
            parametri = " "
            break
        else:
            parametri = " "
           
        
        messaggio = {
            "istruzione":istruzione,
            "parametri":parametri,
        }
        messaggio=json.dumps(messaggio) 
        sock.sendall(messaggio.encode("UTF-8"))
        dati=sock.recv(BUFFER_SIZE)
        ris = json.loads(dati.decode())
        print(ris['valori'])