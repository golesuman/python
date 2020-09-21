secret_num=5
i=0
while i<3 :
	a=int(input('guess_num: '))
	i+=1
	if(a==secret_num):
		print('You were right')
		break
else:
	print('You are wrong')	
	