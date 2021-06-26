#So super is the function that is used to access the method of the parent class without repeating the code

class GiveDimension:
    def __init__(self,length,width) -> None:
        self.length=length
        self.width=width

class Rectangle(GiveDimension):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)
    
    def area(self):
        return self.length*self.width

class Cube(GiveDimension):
    def __init__(self, length, width,height) -> None:
        super().__init__(length, width)
        self.height=height

    def volume(self):
        return self.height*self.width*self.length



area=Rectangle(4,5)
print(area.area())