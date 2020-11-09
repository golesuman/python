class A:
    classvar1='My name is Suman'
    def __init__(self):
        self.classvar1='My name is Ashish'
        self.special="this is special"
        self.var1='this is var1'

class B(A):
    classvar1 = 'hey this is ram'
    def __init__(self):
        self.var1='this is var1 in class b'
        self.classvar1='my name is hari'
        super().__init__()


a=A()
b=B()
print(b.special,b.classvar1,b.var1)
