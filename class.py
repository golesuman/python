class Cat:
    def __init__(self,eye,nose,tail) -> None:
        self.t=tail
        self.n=nose
        self.e=eye

    def name(self):
        print(f'Kitty has {self.t} tail')
    def No_eyes(self):
        print(f"Kitty has {self.e} eye")


kit=Cat(nose=1,tail=2,eye=0)
kit.name()
kit.No_eyes()