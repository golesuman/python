class Animal:
    def __init__(self) -> None:
        pass

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    pass
class Hawk(Animal):
    pass

class Dog(Animal):
    pass


dog=Dog()
dog.eat()
rabbit=Rabbit()
rabbit.sleep()
hawk=Hawk()
hawk.sleep()
