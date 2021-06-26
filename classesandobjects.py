class Human:
    
    def __init__(self,n,o):
        self.name=n
        self.job=o

    def do_work(self):
        if self.job=='Tennis player':
            print(self.name,'play tennis')
        elif self.job=='actor':
            print(self.name,'shoots film')
    def speaks(self):
        print(self.name,'says how are you?')


tom=Human('tom cruise','actor')
tom.do_work()
tom.speaks()