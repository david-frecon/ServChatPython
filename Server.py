import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('',8558))

while True :
    socket.listen(5)
    client,address = socket.accept()
    response = client.recv(255)
    if response != "":
        print(response)


client.close()
socket.close()