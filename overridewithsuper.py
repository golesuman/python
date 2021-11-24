class Parent():
    def altered(self):
        print('Parent Altered')


class Child(Parent):
    def altered(self):
        print('Child, before altered')
        super(Child,self).altered()  # this line will get the parent class for you
        print(f'Child after altered')
father=Parent()
son=Child()
father.altered()
son.altered()