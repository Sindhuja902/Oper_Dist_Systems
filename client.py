import socket
import threading
from datetime import datetime
import random
import time

thread1Timesbefore=[]
thread2Timesbefore=[]
thread1Timesafter=[]
thread2timesafter=[]

def Client():
    host = socket.gethostname()
    # this port should be same as that in server
    port = 4040
    client_socket = socket.socket()
    client_socket.connect((host, port))
    for i in range(10):
        t=((datetime.now()-datetime(1970, 1, 1)).total_seconds())%10000 + random.randint(0,9)*10
        client_socket.send(str(t).encode())
        if(threading.current_thread().name=="thread1"):
            thread1Timesbefore.append(int(float(t)))
        elif(threading.current_thread().name=="thread25"):
            thread2Timesbefore.append(int(float(t)))

        data = client_socket.recv(1024).decode()
        if (threading.current_thread().name == "thread1"):
            thread1Timesafter.append(int(float(data)))
        elif (threading.current_thread().name == "thread25"):
            thread2timesafter.append(int(float(data)))


    client_socket.close()


startTime = datetime.now()
print("client start time:", datetime.now())
threadsList = []
for i in range(50):
    t = threading.Thread(target=Client, name="thread" + str(i))
    t.start()
    threadsList.append(t)
for t in threadsList:
    t.join()
    # this time is when the last client completed its operation

print("client1 Times before","\t","client1 Times after","\t","client2 Times before","\t","client2 times after")
for i in range(10):
    print(thread1Timesbefore[i],"\t",thread1Timesafter[i],"\t",thread2Timesbefore[i],"\t",thread2timesafter[i])
print("delta","\t","delta berkley")
for i in range(10):
    print(thread1Timesbefore[i]-thread2Timesbefore[i],"\t",thread1Timesafter[i]-thread2timesafter[i])
endTime = datetime.now()
print("client end time", datetime.now())
print("Time Taken =", (endTime - startTime).total_seconds() * 100)


