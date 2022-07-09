with open('/home/suman/Downloads/python/gole1.txt', 'a+') as file:
    f = file.write('\nsuman is the best person in the world')
    file.seek(0)
    content = file.read()

print(content)
