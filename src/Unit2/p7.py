#wap to find sum of even num upto n
num=int(input("num: "))
i=1
sum=0
while i<=num:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)