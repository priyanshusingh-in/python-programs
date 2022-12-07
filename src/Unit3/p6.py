#wap to find area of circle square rectangle
import math
def cir(r):
    return math.pi*pow(r,2)
def sqr(l):
    return l*l
def rect(l,b):
    return l*b

r,l,b=int(input()),int(input()),int(input())
print(cir(r),sqr(l),rect(l,b),sep='\n')