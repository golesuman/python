class A:
    val = 10
    
class B(A):
    pass

class C(A):
    pass


class M:
    def print_val(self):
        print(self.val)
        
class D(M, B):
    pass

class E(M, C):
    pass

e = E()
e.print_val()
