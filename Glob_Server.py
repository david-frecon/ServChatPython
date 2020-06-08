from Server import *
from interface import *


serv = ServThread()

panel = Inter(serv)
panel.showpanel()
panel.root.mainloop()
#serv.socket.close()