#classes are the blueprints and objects are the building blocks for the program or the software
#init is used to pass the variables to the function directly using the objectd
class Computer:
    def __init__(self,cpu,ram):
        self.cpu1 = cpu
        self.ram1=ram

    def giveinfo(self):
        print(f'Ram of computer is {self.ram1} and cpu is {self.cpu1}')
c1=Computer('i5',8)
c1.giveinfo()
c2=Computer('i9',16)
c2.giveinfo()