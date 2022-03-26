mark1=[1,2,3,4]
def getmarks(mark1):
    for mark in mark1:
        yield mark


get_marks=getmarks(mark1)


print(get_marks.__next__())
print(get_marks.__next__())
print(get_marks.__next__())
print(get_marks.__next__())



gettingmarks=(x for x in mark1)

print(gettingmarks.__next__())
print(gettingmarks.__next__())
