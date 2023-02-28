# Here __init is automatically called
# and for every object it will call exactly once

class Comp:

    def __init__(self,cpu,ram):
        print("init")
        self.cpu = cpu
        self.ram = ram

    def cofi(self):
        print("config",self.cpu,self.ram)

comp1 = Comp('i5 ',16)
comp2 = Comp('Ryzen 3 ',8)

comp1.cofi()
comp2.cofi()



