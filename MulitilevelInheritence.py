class Orgasm:
    alive=True

class Animal(Orgasm):
    def eat(self):
        print(f'The animal is eating')

class Dog(Animal):
    def bark(self):
        print(f'The animal is barking')

class Cat(Dog):
    def scratch(self):
        print(f'The animal is scratching.')


mit=Cat()
mit.eat()
mit.bark()