from socket import *

HOST = '127.0.0.1'
PORT = 9823

try:
    client = socket(AF_INET, SOCK_STREAM)
    print("TCP client socket created successfully")
except:
    print("TCP client socket creation failed!")

client.connect((HOST, PORT))

message = input("Input lowercase message: ")
client.send(message.encode())
modified_msg = client.recv(1024)
print("Response from TCP server: ", modified_msg.decode())

client.close()