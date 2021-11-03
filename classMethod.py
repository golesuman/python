class Employee:

    raised=1.05

    def __init__(self,name,address,salary):
        self.name = name
        self.email = self.name+'@gmail.com'
        self.salary=salary
        self.address = address

    def getDetails(self):
        return print(f'Name is {self.name} And He lives in {self.address} and email is {self.email}@gmail.com,\
            salary:{self.salary*self.raised}')

    @classmethod
    def new_raise(cls,new_raised):
        cls.raised=new_raised
    

e1=Employee('Hari',address='kathmandu',salary=10000)
e1.getDetails()
e1.new_raise(1.07)
e1.getDetails()
print(Employee.raised)
