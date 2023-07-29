#This is lecture no 24 in which we learn about init method
#init method is same as constructor in c++
#Or tm ek chiz notice kiya hoga ki jitna object bnaya us sbka pehle constructor call ho jaega
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Configuration is",self.cpu,self.ram)


comp1=Computer('i5',16)
comp2=Computer('Ryzen',8)

comp1.config()
comp2.config()