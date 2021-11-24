class Parent:
    def whoamI(self):
        print(f'I am the father')



class Child(Parent):
    def whoamI(self):
        print(f'I am the son')


father=Parent()
child=Child()
father.whoamI()
child.whoamI()