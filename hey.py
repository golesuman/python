list=[5,6,7,8]
for numbers in list:
    print('x'*numbers )



for numbers in list:
    output=""
    for items in range(numbers):
        output+="x"
    print(output)
    ls=[1,5,8,79,21,4,2,63]
max=ls[2]
for number in ls:
    if (max<number):
        max=number
print(f'{number} is the greatest number')
def factorial(num):
    if (num==0) or (num==1):
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))
def factorial_iter(n):
    product=1
    for num in range(1,n+1):
        product=product*num
    return product
print(factorial_iter(5))