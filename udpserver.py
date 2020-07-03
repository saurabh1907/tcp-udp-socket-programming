from socket import *

HOST = '127.0.0.1'
PORT = 9823

try: 
    server = socket(AF_INET, SOCK_DGRAM)
    print("UDP server socket created successfully")
except error as err: 
    print("UDP socket creation failed!")

server.bind((HOST, PORT))

print("UDP server ready to receive")

while True:
    message, client_addr = server.recvfrom(1024)
    print("New message received from client - ", client_addr)
    modified_msg = message.decode().upper()
    server.sendto(modified_msg.encode(), client_addr)
