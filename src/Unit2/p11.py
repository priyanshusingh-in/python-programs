num=int(input("num1: "))
i=0
sum=0
while i<=num:
        sum+=i
        i=i+1
else:
    while num<=0:
        sum+=num
        num=num+1
print(sum)