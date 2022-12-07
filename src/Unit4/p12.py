data1=input('data1:')
data2=input('data2:')
list1=data1.split(',')
list2=data2.split(',')
dict1=dict(zip(list1,list1))
l1=[]
for key in dict1:
    l1.append(dict1[key])
l1.sort()
print('max:',l1[-1])
print('min:',l1[0])