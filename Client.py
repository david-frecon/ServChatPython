import socket

host = "localhost"
port = 8558

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

print("connection {}".format(port))

while True:
    data = input()
    socket.send(data.encode("utf8"))

socket.close()
