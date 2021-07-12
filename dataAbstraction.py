from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
class car(Vehicle):
    def go(self):
        print("The you can go now")
    
    def stop(self):
        print(f"you can stop")
class Motorcycle(Vehicle):
    def go(self):
        print("You can go now motorcycle")
    def stop(self):
        print("Your motorcycle can stop now")

# vehicle=Vehicle()
car=car()
motorcycle=Motorcycle()