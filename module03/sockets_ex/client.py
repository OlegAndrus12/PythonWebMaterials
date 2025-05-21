import socket


host = socket.gethostname()
port = 12344
client = socket.socket()
client.connect((host, port))

message = input("--> ")

while message != "end":
    client.send(message.encode())
    data = client.recv(100).decode()
    print("Received message: ", data)
    message = input("--> ")

client.close()
