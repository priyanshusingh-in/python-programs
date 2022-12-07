data1=input()
data2=input()
l1=data1.split()
l2=data2.split()
l3=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
        l1[i]=int(l1[i])
        l2[i]=int(l2[i])
        l3.append(abs(int(l1)-int(l2)))
    print(l3)
else:
    print("lists are different lengths")