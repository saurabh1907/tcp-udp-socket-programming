from socket import *

HOST = '127.0.0.1'
PORT = 9823

client = socket(AF_INET, SOCK_DGRAM)

client.connect((HOST, PORT))

message = input("Input lowercase message: ")
client.send(message.encode())
modified_msg = client.recv(1024)
print("Response from UDP server: ", modified_msg.decode())

client.close()