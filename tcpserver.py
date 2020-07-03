from socket import *

HOST = '127.0.0.1'
PORT = 9823

try:
    server = socket(AF_INET, SOCK_STREAM)
    print("TCP server socket created successfully")
except:
    print("TCP server socket creation failed!")

server.bind((HOST, PORT))
server.listen(5) # max number of connections allowed

print("TCP server is ready to receive")

connection_socket, client_addr = server.accept()

with connection_socket as conn_skt:
    message = conn_skt.recv(1024).decode()
    print("New message received from client - ", client_addr)
    msg_uppercase = message.upper()
    conn_skt.send(msg_uppercase.encode())