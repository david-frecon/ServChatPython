import socket
import threading
from tkinter import *
import time

#print("connection {}".format(port))

class RecoverMessage(threading.Thread):
    def __init__(self,conn,log,Chat):
        threading.Thread.__init__(self)
        self.conn = conn
        self.log = log
        self.chat = Chat
    def run(self):
        while True:
            self.message = self.conn.recv(1024)
            if self.message.decode("utf8") == "/rmuteuser":
                self.chat.config(state = DISABLED)
                time.sleep(30)
                self.chat.config(state = "normal")
            else :
                self.log.insert(END,self.message)

class Client():
    def __init__(self, host = "localhost", port = 8558):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))


    def GiveLog(self,log,chat):
        self.log = log
        self.RecMess = RecoverMessage(self.socket, self.log,chat)
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