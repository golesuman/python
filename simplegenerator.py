def generate(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k


print(generate(6))
