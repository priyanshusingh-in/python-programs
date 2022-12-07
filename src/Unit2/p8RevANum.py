n=int(input("Enter a number: "))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print(r)

#Alternative Method

num=int(input("Enter a number: "))
revNum=""
while num==0:
    revNum=revNum+(num%10)
    num=num//10
