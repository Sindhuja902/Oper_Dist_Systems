import socket
from datetime import datetime
import time

localTimesOfClients = []

def Server():
    host = socket.gethostname()
    port = 4040
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(50)
    print("server started !!", datetime.now())
    clientTimes=[]
    connectionsList = []
    for i in range(50):

        conn, address = server_socket.accept()
        global localTimesOfClients
        connectionsList.append((conn, address))

    for i in range(10):
        for con,add in connectionsList:
            t=(con.recv(1024).decode())
            clientTimes.append(float(t))

        avgTime=sum(clientTimes)/len(clientTimes)
        clientTimes=[]
        for con,add in connectionsList:
            con.send(str(avgTime).encode())
        time.sleep(1)
    for con, add in connectionsList:
        con.close()

    server_socket.close()



Server()


