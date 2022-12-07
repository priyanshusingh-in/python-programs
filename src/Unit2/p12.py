#wap to print fibonacci series upto n terms
n=int(input())
a=0
b=1
c=0
i=1
str=""
while i<=n:
    c=a+b
    
    temp=a
    a=b
    b=temp
    print(c)
    i+=1
