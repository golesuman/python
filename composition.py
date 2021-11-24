class Parent():
    def altered(self):
        print("Parent altered")

    def override(self):
        print(f'Parent Override')


class Child():
    def __init__(self) -> None:
        self.father=Parent()


    def override(self):
        self.father.override()

    def altered(self):
        self.father.altered()


son=Child()
son.altered()
son.override()
