import socket

def client_program():
    host = socket.gethostname()
    port = 5001
    client_socket = socket.socket()
    client_socket.connect((host, port))
    msg = input(" >>> ")
    while msg.lower().strip() != 'bye':
        client_socket.send(msg.encode())
        data = client_socket.recv(32768).decode()
        print('Message received from the server: ' + data)
        msg = input(" >>> ")
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()