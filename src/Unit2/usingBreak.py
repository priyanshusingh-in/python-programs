#using break in a loop

for i in range(10):
    print(i)
    if i == 2:
        break

print("##########################")

i=1
while(i<10):
    if(i%2==0):
        print(i)
        break
    i=i+1
else:
    print("Bread")