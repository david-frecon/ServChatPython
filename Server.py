import socket
import threading
import tkinter as tk

## init the server
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('',8558))

## init the windows




print("yay")

class ThreadChat(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        message = self.conn.recv(1024)
        message = message.decode("utf8")
        th1.textbox.insert(tk.END, message+"\n")


class interface(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fen = tk.Tk()
        self.fen.geometry("800x800")

        self.textbox = tk.Text(self.fen)
        self.textbox.pack()
        self.button = tk.Button(self.fen, text="exit", command=self.fen.quit)
        self.button.pack()
        self.fen.mainloop()



th1 = interface()
th1.start()

th1.textbox.insert(tk.END,"The server is init\n")
while True :
    socket.listen(5)
    client,address = socket.accept()
    th1.textbox.insert(tk.END, "A client is connect\n")
    print("A client is connect")
    conn = ThreadChat(client)
    conn.start()


client.close()
socket.close()
