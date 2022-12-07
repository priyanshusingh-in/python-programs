s1=input()
l1=s1.split(',')
t1=tuple(l1)
print(t1j)
index=int(input())
size=len(t1)
if index != -1:
    if index<len(t1) and len(l1)>=-(size):
        t2=t1[:index]+t1[index+1:]
        print('after removing:',t2)
    else:
        print('enter valid index')
else:
    print('after removing:',t1[:index])