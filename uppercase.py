print("What's your name?")
name=input("Name:")
if len(name)<3:
	print("Name must be at least of 3 characters")
elif len(name)>50:
	print("Name can not exceed 50 characters")
else:
	print("You are good to go")