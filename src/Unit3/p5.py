def addavg(a,b):
    return a+b,(a+b)/2

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

a=int(input())
b=int(input())

print(addavg(a,b))
print(sub(a,b))
print(mul(a,b))