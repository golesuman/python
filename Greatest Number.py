def great(a,b,c):
    if a>b and a>c:
        return print(f'{a} is the greatest number')
    elif b>c and b>a:
        return print(f'{b} is the greatest number')
    else:
        return print(f'{c} is the greatest number')
g=great(23,245,5)
print(g)