from tkinter import *
from tkinter.messagebox import *

class InterConn():
    def __init__(self, client):
        self.root = Tk()
        self.client = client
        #self.root.geometry("800x800")
        self.root.resizable(False,False)
        self.lab = Label(self.root, text = "Salon de connection")
        self.LabPseudo = Label(self.root, text = "Pseudo")
        self.LabHost = Label(self.root, text="Host")
        self.LabPort = Label(self.root, text="Port")
        self.pseudo = StringVar()
        self.host = StringVar()
        self.port = StringVar()
        self.entpseudo = Entry(self.root, textvariable = self.pseudo, relief = "flat")
        self.enthost = Entry(self.root, textvariable = self.host, relief = "flat")
        self.entport = Entry(self.root, textvariable = self.port, relief = "flat")
        self.btn = Button(self.root, text = "Confimation", command = self.Confirmation)


    def Confirmation(self):
        self.pseudo2 = self.pseudo.get()
        self.host2 = self.host.get()
        self.port2 = self.port.get()
        if self.pseudo2 == "" or self.host2 == "" or self.port2 == "":
            showwarning(title = "Mauvaise entrée", message = "Tous les champs doivent être remplie")
        else :
            self.interclient = InterClient(self.client)
            self.interclient.panel()
            self.interclient.root.mainloop()



    def SetPanel(self):
        self.lab.grid(row = 0, column = 2)
        self.LabPseudo.grid(row = 1, column = 2)
        self.LabHost.grid(row=3, column=0)
        self.LabPort.grid(row=3, column=3)
        self.entpseudo.grid(row = 2, column = 2)
        self.enthost.grid(row = 4, column = 0)
        self.entport.grid(row = 4, column = 3)
        self.btn.grid(row = 4, column = 1)


"""test = InterConn()
test.SetPanel()
test.root.mainloop()"""




class InterClient():
    def __init__(self,client):
        self.root = Tk()
        self.root.resizable(False, False)
        self.client = client
        self.message = StringVar()
        self.log = Text(self.root, relief = "flat", bg = "#FFFFFF" )
        self.Chat = Entry(self.root, textvariable = self.message, relief = "flat", bg = "#FFFFFF")
        self.btn = Button(self.root, text = "Dark", command = self.ChangeTheme)
        self.btn2 = Button(self.root, text = "SEND", command = self.SendMessage)
        self.client.GiveLog(self.log,self.Chat)
        self.root.bind('<Return>', self.SendMessage)

    def ChangeTheme(self):
        if self.btn.cget("text") == "Dark":
            self.btn.config(text = "Light", bg = "#6566EC",fg = "#FFFFFF")
            self.root.config(bg = "#2f3640")
            self.log.config(bg = "#49525E",fg = "#FFFFFF")
            self.btn2.config(bg = "#2f3640",fg = "#FFFFFF")
            self.Chat.config(bg = "#49525E",fg = "#FFFFFF")
        else :
            self.btn.config(text="Dark", bg="#FFFFFF",fg = "#000000")
            self.root.config(bg="#BBC5D2")
            self.log.config(bg="#FFFFFF",fg = "#000000")
            self.btn2.config(bg="#FFFFFF",fg = "#000000")
            self.Chat.config(bg="#FFFFFF",fg = "#000000")

    def SendMessage(self,event):
        if self.message.get() != "":
            self.client.SendMessage(self.message.get()+"\n")
            self.Chat.delete(0,END)

    def panel(self):
        #self.frame1.grid(row = 0, column = 0,sticky = "WE")
        #self.frame2.grid(row = 1, column = 0,sticky = "WE")
        #self.frame3.grid(row = 0, column = 3,sticky = "WE")
        #self.frame4.grid(row = 1, column = 3,sticky = "WE")


        self.log.grid(row = 0, column = 0,sticky = "WE")
        self.Chat.grid(row = 1, column = 0,sticky = "WE")
        self.btn.grid(row = 0, column = 3,sticky = "sew")
        self.btn2.grid(row = 1, column = 3,sticky = "WE")


"""
        for frame,text in [("1","Log"),("2","Chat"),("3", "Theme"),("4","")]:
            exec("self.frame"+frame+"=LabelFrame(self.root, text = '"+text+"')")
"""