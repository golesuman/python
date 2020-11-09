class A:
    def a(self):
        print(f'this is in class a')
class B(A):
    def a(self):
        print(f'this is is in class b')
class C(A):
    def a(self):
        print(f'this is in class c')
class D(B, C):
    pass
    def a(self):
        print(f'this is in class d')
clA=A()
clB=B()
clC=C()
clD=D()
clD.a()
clA.a()