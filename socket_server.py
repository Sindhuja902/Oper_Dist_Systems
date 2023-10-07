import socket
def server_program():

    host = socket.gethostname()
    port = 5001
    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection is from: " + str(address))
    while True:
        data = conn.recv(32768).decode()
        if not data:
            break
        print("Message from the connected user: " + str(data))
        data = input(' >>> ')
        conn.send(data.encode())
    conn.close()
if __name__ == '__main__':
    server_program()