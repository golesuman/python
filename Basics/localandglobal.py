x = 10
def show():
    x = 5
    return x

print(show())
# print(x)

def outer(): # function inside function
    x = 10
    def inner(x):
        print(x)

    inner(x)

outer()




