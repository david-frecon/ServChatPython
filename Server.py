import socket
import threading
import tkinter as tk

## init the server
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('',8558))

## init the windows
fen = tk.Tk()
fen.geometry("800x800")






print("The server is init ")

class ThreadChat(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        message = self.conn.recv(1024)
        message = message.decode("utf8")
        print(message)



while True :
    socket.listen(5)
    client,address = socket.accept()
    print("A client is connect")
    conn = ThreadChat(client)
    conn.start()
        


client.close()
socket.close()