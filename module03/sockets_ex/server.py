import socket


host = socket.gethostname()
port = 12344

server = socket.socket()
server.bind((host, port))
server.listen(2)

conn, address = server.accept()

while True:
    message = conn.recv(100).decode()
    if not message:
        break

    print("Received message: ", message)
    message = input("-->")
    conn.send(message.encode())

conn.close()
