import socket
import threading
import interface
from tkinter import *
import time
"""
## init the server
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('',8558))

## init the windows
"""


all_client = []
print("1yay")


class UpdateListBox(threading.Thread):
    def __init__(self,listbox):
        threading.Thread.__init__(self)
        self.totalpseudo = ""
        self.listbox = listbox
    def run(self):
        while True:
            tot = ""
            for conn, client in all_client:
                if client.pseudo == "":
                    ip,port = client.address
                    tot += ip
                else:
                    tot += client.pseudo[1:-1]
            if tot != self.totalpseudo:
                self.totalpseudo = tot
                self.listbox.delete(0,END)
                for conn, client in all_client:
                    if client.pseudo == "":
                        ip, port = client.address
                        self.listbox.insert(END,ip)
                    else:
                        self.listbox.insert(END,client.pseudo[1:-1])




class ThreadChat(threading.Thread):
    def __init__(self,conn,log,socket,address):
        global all_client
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.conn = conn
        self.log = log
        self.pseudo = ""
        self.mute = False
    def run(self):
        global all_client
        for i in all_client:
            print(i)
        while True :
            print(self.mute)
            if not self.mute:
                print("france")
                message = self.conn.recv(4096)
                message = message.decode("utf8")
                print(message[0:7])
                if message[0:8] == "pseudo :":
                    self.pseudo = "["+message[9:-1]+"]"
                    print(self.pseudo)
                else:
                    message = self.pseudo+ message
                    self.log.insert(END,message)
                    self.SendAllClient(message)
            else :
                self.conn.send("/rmuteuser".encode("utf8"))
                time.sleep(30)
                self.mute = False

    def UnMute(self):
        self.mute = False
    def SendAllClient(self,message):
        global all_client
        if message != "" and message != "\n" :
            for conn, client in all_client:
                conn.send(message.encode("utf8"))



class ServThread (threading.Thread):
    def __init__(self,host = "", port = 8558):
        global all_client
        threading.Thread.__init__(self)
        self.ListClient = []
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((host,port))
    def GiveParameter(self,log, listbox):
        self.log = log
        self.update = UpdateListBox(listbox)
        self.update.start()

    def run(self):
        global all_client
        while True:
            self.socket.listen()
            self.conn, self.address = self.socket.accept()
            #self.conn.setblocking(0)
            #self.conn.settimeout(0)
            self.client = ThreadChat(self.conn, self.log,self.socket,self.address)
            self.ListClient.append((self.client, self.conn))
            all_client.append((self.conn,self.client))
            self.client.start()
    def SendAllClient(self,message):
        global all_client
        if message != "" and message != "\n":
            for conn, client in all_client:
                conn.send(message.encode("utf8"))

    def Mute2(self, pseudo):
        print("recherche")
        for conn, client in all_client:
            ip,_ = client.address
            #print(ip + " " + client.pseudo)
            if client.pseudo[1:-1] == pseudo or ip == pseudo :
                print(pseudo + " "+ ip + " " + client.pseudo)
                client.mute = True
















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
        #self.client.close()
        #self.socket.close()










"""
while True :
    socket.listen(5)
    client,address = socket.accept()
    print("A client is connect")
    conn = ThreadChat(client)
    conn.start()



client.close()
socket.close()"""
