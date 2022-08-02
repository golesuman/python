from numpy import full


class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.fullname = first + " " + last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}@gmail.com"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

        return self.first + " " + self.last



e = Employee("Suman", "Gole")
e.first = "Hari"
e.fullname = "radhe shyam"
print(e.email)
print(e.first)
print(e.fullname)
# print()
