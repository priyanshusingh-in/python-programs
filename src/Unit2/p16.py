#wap to print all the multiples of three bw 10 to 50 both inclusive

#using while-loop
i=10
while(i<=50):
    if(i%3==0):
        print(i)
    i=i+1

#using for-loop
for i in range(10,51):
    if(i%3==0):
        print(i)