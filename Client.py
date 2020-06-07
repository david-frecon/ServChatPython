import socket
import threading
from tkinter import *


#print("connection {}".format(port))

class RecoverMessage(threading.Thread):
    def __init__(self,conn,log):
        threading.Thread.__init__(self)
        self.conn = conn
        self.log = log
    def run(self):
        while True:
            self.message = self.conn.recv(1024)
            self.log.insert(END,self.message)

class Client():
    def __init__(self, host = "localhost", port = 8558):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))


    def GiveLog(self,log):
        self.log = log
        self.RecMess = RecoverMessage(self.socket, self.log)
        self.RecMess.start()

    def SendMessage(self, message):
        self.socket.send(message.encode("utf8"))


"""
rec = RecoverMessage(socket)
rec.start()
while True:
    data = input()
    socket.send(data.encode("utf8"))

socket.close()
"""