import socket

host = "localhost"
port = 8558

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))

socket.send(input())

socket.close()