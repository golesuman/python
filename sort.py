students=[('squidward','F',60),
        ('sandy','C',33),
        ('Patrck','D',55),
        (' Suman','F',93)]

age=lambda ages:ages[2]
students.sort(key=age,reverse=True)
for name in students:
    print(name)