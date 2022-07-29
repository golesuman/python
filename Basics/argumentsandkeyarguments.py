

def Addtion(*args):
    sum = 0
    for item in args:
        sum += item
    return sum



def keyAddtion(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}", end=" ")



if __name__ == "__main__":
    print(Addtion(3,4,5))
    keyAddtion(name = "Suman", address = "Kathmandu")

