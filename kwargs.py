def get_name(**kwargs):
    for key,val in kwargs.items():
        print(val,end=' ')

get_name(Firstname='suman',Lastname='Gole')

def add(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum
print(add(5,6,7,2))

