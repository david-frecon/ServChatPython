from InterfaceClient import *
from Client import *

client = Client()

inter = InterClient(client)
inter.panel()
inter.root.mainloop()
