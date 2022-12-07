s1=input()
l1=s1.split(',')
t1=tuple(l1)
index=int(input())
value=int(input())
if index<len(l1) and len(l1)>=-(index):
    l1[index]=value
else:
    print('enter valid index')
print(t1)

