prices=[10,20,30]
total=0
for price in prices:
    total=total+price
print(f'The total price is {total}')
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers=[1,1,1,1,5]
for items in numbers:
    print('x'*items)



for x_count in numbers:
    output=''
    for number in range(x_count):
        output+='x'
    print(output)


