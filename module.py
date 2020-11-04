a=int(input("Enter the number of a:"))
b=int(input("Enter the name of b:"))
def sub(a,b):
    s=a-b
    return print(s)
def add(a,b):
    a=a+b
    return print(a)
def main():
    add(a,b)
    sub(a,b)
if __name__=='__main__':
    main()