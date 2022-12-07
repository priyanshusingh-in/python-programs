def add(x,y):
    """This function will add the parameters"""
    print(x+y)
def sub(x,y):
    """This function will subtract the parameters"""
    print(x-y)
def mul(x,y):
    """This function will multiply the parameters"""
    print(x*y)
x=int(input("x: "))
y=int(input("y: "))
print(add.__doc__)
add(x,y)
print(sub.__doc__)
sub(x,y)
print(mul.__doc__)
mul(x,y)