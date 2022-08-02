class Animal():
    def __init__(self, name) -> None:
        self.name = name


    def walk(self):
        return f"{self.name} walks"


class Cat(Animal):
    def __init__(self, name, typeofcolor) -> None:
        super().__init__(name)
        self.typeofanimal = typeofcolor


    def walk(self):
        return f"{self.name} of {self.typeofanimal} color walks like this "



class Dog(Animal):
    def __init__(self, name, typeofear, nooflegs) -> None:
        super().__init__(name)
        self.typeofear = typeofear
        self.nooflegs = nooflegs

    def show_details(self):
        return f"My dog {self.name} has {self.typeofear} ears and {self.nooflegs} legs"



if __name__ == "__main__":
    cat1 = Cat("Marim", "white")
    print(cat1.walk())
    dg = Dog("Sandy", "pointy", 4)
    print(dg.show_details())