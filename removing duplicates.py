numbers=[2,5,2,7,8,8,9,0]
unique=[ ]
for number in numbers:
	if number not in unique:
		unique.append(number)
print(unique)