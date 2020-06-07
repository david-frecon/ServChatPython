from tkinter import *
from tkinter import font
#from Server import serv

class Inter():
    def __init__(self, serv):
        self.root = Tk()
        self.serv = serv
        self.font = font.Font(family='Ubuntu', weight='bold')
        self.root.resizable(False,False)
        for frame, text in [("1","Option Serveur"),("2","Mod Chat"),("3","Option du server"),("4","Log"),("5","Thème"),("6","List")]:
            exec ("self.frame"+frame+"=LabelFrame(self.root,text = '"+text+"')")

        for number in "123":
            self.frame2.columnconfigure(int(number), weight=1)
        self.frame1.columnconfigure(0, weight=1)

        self.but1 = Button(self.frame1,text = "ON",  bg='#fbc531', fg="#FFFFFF",font=self.font,bd=0, command = self.StartServ)
        self.but2 = Button(self.frame3, text="Mute", state=DISABLED, fg="#f1c40f",
                                   font=font.Font(family='Ubuntu', size=10, weight='bold'), bd=0)
        self.but3 = Button(self.frame3, text="kick", state=DISABLED, fg="#f1c40f",
                           font=font.Font(family='Ubuntu', size=10, weight='bold'), bd=0)
        self.but4 = Button(self.frame3, text="ban", state=DISABLED, fg="#f1c40f",
                           font=font.Font(family='Ubuntu', size=10, weight='bold'), bd=0)
        self.message = StringVar()
        self.chat = Entry(self.frame2,state = DISABLED,textvariable = self.message, relief = "flat", bg = "#FFFFFF")

        self.log = Text(self.frame4,state = DISABLED, relief = "flat")
        self.theme = Button(self.frame5, text="DARK", bg="#2f3640", fg="#FFFFFF",
                                    font=font.Font(family='Ubuntu', size=10, weight='bold'),
                                    relief="groove", bd=0, command = self.selecttheme)
        self.users = Listbox(self.frame6, selectbackground="#9b59b6", activestyle="none", bd=0,
                                     highlightthickness=1, highlightcolor="#9b59b6")
        self.root.bind('<Return>', self.SendMessage)

    def selecttheme(self):
        if self.theme.cget("text") == "DARK":
            self.theme.config(text = "LIGHT",bg = "#6566EC")
            self.root.config(bg = "#2f3640")
            self.log.config(bg = "#2f3640", fg = "#FFFFFF")
            self.chat.config(bg="#2f3640", fg="#FFFFFF", disabledbackground="#2f3640")
            self.users.config(bg = "#2f3640", fg = "#FFFFFF")

            for number in "123456":
                exec("self.frame"+number+".config(bg = \"#2f3640\", fg = \"#FFFFFF\")")
            for item in ["2","3","4"]:
                exec("self.but"+item+".config(bg = \"#2f3640\", fg = \"#FFFFFF\")")

        else :
            self.theme.config(text = "DARK",bg="#2f3640", fg="#FFFFFF")
            self.root.config(bg="#FFFFFF")
            self.log.config(bg="#FFFFFF", fg="#000000")
            self.chat.config(bg="#FFFFFF", fg="#000000", disabledbackground="#FFFFFF")
            self.users.config(bg="#FFFFFF", fg="#000000")

            for number in "123456":
                exec("self.frame" + number + ".config(bg = \"#FFFFFF\", fg = \"#000000\")")
            for item in ["2", "3", "4"]:
                exec("self.but" + item + ".config(bg = \"#FFFFFF\", fg = \"#000000\")")

    def SendMessage(self,event):
        self.log.insert(END,self.message.get()+"\n")
        self.chat.delete(0,END)

    def ModifyState(self, state):
        for i in ["but2","but3","but4", "chat","log"]:
            exec("self."+i+".config(state = '"+state+"' )")

    def StartServ(self):
        if self.but1.cget("text")=="ON":
            self.but1.config(text = "OFF", bg = "#ED0B0B")
            self.ModifyState("normal")
            self.log.insert(END,"Le serveur demarre ...\n")
            self.serv.GiveLog(self.log)
            self.serv.start()
        else :
            self.but1.config(text="ON", bg="#fbc531")
            self.log.insert(END, "Le serveur s'éteint ...\n")
            self.ModifyState("disable")



    def showpanel(self):
        self.frame1.grid(row = 0, column =0)
        self.frame2.grid(row = 0, column = 1)
        self.frame3.grid(row = 0, column = 2)
        self.frame4.grid(column=0, row=1, columnspan=3)
        self.frame5.grid(row = 2, column = 0)
        self.frame6.grid(row = 2, column = 2)

        self.but1.grid(sticky='we')
        self.chat.grid(sticky = "WE")
        self.but2.grid(row=0,column=1, sticky='WE')
        self.but3.grid(row=0, column=2, sticky='WE')
        self.but4.grid(row=0, column=3, sticky='WE')
        self.log.grid(sticky="we")
        self.theme.grid(sticky = "we")
        self.users.grid(sticky = "we")
"""panel = fenetre()
panel.showpanel()
panel.root.mainloop()"""
