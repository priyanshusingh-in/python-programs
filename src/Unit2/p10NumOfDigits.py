#wap to find number of digits in a number
n=int(input("enter a num: "))
nDigit=0
while n>0:
    n=n//10
    nDigit=nDigit+1
print(nDigit)