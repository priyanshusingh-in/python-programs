s1=input('data: ')
lis1=s1.split()
size=len(lis1)
for i in range(size):
    lis1[i]=int(lis1[i])
count=0
element=int(input('element: '))
for i in range(0,len(lis1)):
    if lis1[i]==element