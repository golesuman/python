n=int(input('Enter the number:'))
for i in range(1,10):
    print(f'{n}X{i}={n*i}')

l1=["Harry",'Soham','Sachin','Rahul']
for name in l1:
    if name.startswith('H'):
        print(f'Greetings {name}')
    if name.startswith('S'):
        print(f'Hello {name}')
    if name.startswith('R'):
        print(f'Hello {name}')
num=int(input('Enter the num: '))
prime=True
for number in range(2,num):
    if(num%number==0):
        prime=False
        print('The number is not prime')
        break
if prime:
    print('The number is prime')

num = int(input('Enter the number:'))
i = 1
total = 0
while i <= num:
    total = total + i
    i += 1



print(total)

total1=0

for i in range(1,6):
    total1=to
