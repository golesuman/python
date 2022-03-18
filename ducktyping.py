class Duck():
    def walk(self):
        print('the duck is walking')


    def talk(self):
        print("the duck is talking")


class Chicken():

    def walk(self):
        print("the chicken is walking")


    def talk(self):
        print("the chicken is talking")



class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()


        print("you catched it")


p1=Person()
chicken=Chicken()

duck=Duck()
p1.catch(chicken)
