print("Multiplication Table")
#Display the number title
print("|",end='')
for j in range(1,11):
    print("",j,end='')
print()
print("---------------------------------------------------------------")
#Display table body
for i in range(1,11):
    print(i,"|",end='')
    for j in range(1,11):
        print(i*j,"  ",end='')
    print()