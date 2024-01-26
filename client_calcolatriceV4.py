import json
import socket
import socket
import sys
from random import *
import os
import time
import threading
import multiprocessing

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 2048
NUM_WORKERS = 15

def genera_richieste(addres, port):
    try:
        start_time_thread = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP,SERVER_PORT))
    except:
        print(f"{threading.current_thread().name} non si collega")
    primoNumero = randint(1,15)
    i=randint(0,4)
    op=["+","-","*","/","%"]
    operazione=op[i]
    secondoNumero = randint(1,15)
    messaggio ={'primoNumero': primoNumero,
                'operazione': operazione,
                'secondoNumero': secondoNumero}
    messaggio = json.dumps(messaggio) #Trasformiamo l'oggetto in una stringa
    s.sendall(messaggio.encode("UTF-8"))
    data = s.recv(BUFFER_SIZE)
    print("Risultato : ",data.decode())
    end_time_thread = time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione =", end_time_thread - start_time_thread)

if __name__ == '__main__':
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste,args=(SERVER_IP, SERVER_PORT))for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("Total threads time=", end_time - start_time)


