import socket
import threading
from tkinter import *
import time


class RecoverMessage(threading.Thread):
    def __init__(self,conn,log,Chat):
        threading.Thread.__init__(self)
        self.conn = conn
        self.log = log
        self.chat = Chat
        self.is_running = True

    def terminate(self):
        self.is_running = False
    def run(self):
        while self.is_running:
            self.message = self.conn.recv(1024)
            if self.message.decode("utf8") == "/rmuteuser":
                self.chat.config(state = DISABLED)
                time.sleep(30)
                self.chat.config(state = "normal")
            else :
                self.log.insert(END,self.message)

class Client():
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def ter(self):
        self.RecMess.terminate()

    def GiveLog(self,log,chat):
        self.log = log
        self.RecMess = RecoverMessage(self.socket, self.log,chat)
        self.RecMess.start()

    def SendMessage(self, message):
        self.socket.send(message.encode("utf8"))


