import socket
import threading
import interface
from tkinter import *
"""
## init the server
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('',8558))

## init the windows
"""



print("1yay")

class ThreadChat(threading.Thread):
    def __init__(self,conn,log,socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.conn = conn
        self.log = log
    def run(self):
        while True :
            message = self.conn.recv(1024)
            message = message.decode("utf8")
            self.log.insert(END,message)
            self.conn.send(message.encode("utf8"))


class ServThread (threading.Thread):
    def __init__(self,host = "", port = 8558):
        threading.Thread.__init__(self)
        self.ListClient = []
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((host,port))

    def GiveLog(self,log):
        self.log = log

    def run(self):
        while True:
            self.socket.listen()
            self.conn, self.address = self.socket.accept()
            self.client = ThreadChat(self.conn, self.log,self.socket)
            self.ListClient.append((self.client, self.conn))
            self.client.start()
    def SendAllClient(self,message):
        for c,h in self.ListClient:
            self.h.send(message)




class ChatServ():
    def __init__(self,host = "", port = 8558):
        self.ListClient = []
        self.host = host
        self.port = port
        #self.log = log
    def Start(self,log):
        self.log = log
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host,self.port))
        while True:
            self.socket.listen()
            self.conn, self.adress =  self.socket.accept()
            self.log.insert(END,"Un client c'est connecté{}".format(self.adress))
            self.client = ThreadChat(self.conn,self.log)
            self.client.start()
    def Stop(self):
        self.log.insert(END,"Le server est déconnecter")
        self.client.close()
        self.socket.close()










"""
while True :
    socket.listen(5)
    client,address = socket.accept()
    print("A client is connect")
    conn = ThreadChat(client)
    conn.start()



client.close()
socket.close()"""
