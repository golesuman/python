class Prey:
    def prey(self):
        print(f'It is prey')

class Predator:
    def predator(self):
        print('It is predator')

class Cat(Prey):
    def cat(self):
        print('It is prey')


class Dog(Predator,Prey):
    def dog(self):
        print('Dog is predator')


dog=Dog()
dog.prey()
dog.predator()
dog.dog()
