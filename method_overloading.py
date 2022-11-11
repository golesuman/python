class Adder:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        
        return Adder(x, y)
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
        
a1 = Adder(2, 3)
a2 = Adder(3, 4)
print(a1 + a2)
        
        
        
