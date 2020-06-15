from InterfaceClient import *
from Client import *
import threading
import time

class ThreadClient2 (threading.Thread):
    def __init__(self, conn):
        self.con = conn
        threading.Thread.__init__(self)
    def run(self):
        while(not self.con.bool):
            pass
        self.con.root.quit()
        #time.sleep(5)
        self.client = Client(self.con.socket)
        time.sleep(5)
        inter = InterClient(self.client)
        inter.panel()
        inter.root2.mainloop()
        print("fin 2 fenetre")
        self.con.socket.send("/rquit".encode("utf8"))
        self.con.socket.close()
        self.client.ter()


connection = InterConn()
connection.SetPanel()
connection.root.mainloop()
ttttt = ThreadClient2(connection)
ttttt.run()




