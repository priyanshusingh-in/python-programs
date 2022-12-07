#print all prime number for the given range
rag=int(input())
for num in range(2,rag+1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)