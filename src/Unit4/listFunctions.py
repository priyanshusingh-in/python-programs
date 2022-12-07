#all()
ls=['hello','hi','dog','car']
print(all(ls))

ls=[False,'hi','dog','car']
print(all(ls))

#enumerate()
ls=['hello','hi','dog','car']
print(list(enumerate(ls)))

#len()
ls=[False,'hi','dog','car']
print(len(ls))

#list()
ls=[False,'hi','dog','car']
print(list(ls))

#sorted() for ascending and sorted(list,reverse=True) for descending 
ls=[1,2,3,4]
print(sorted(ls))
print(sorted(ls,reverse=True))

#sum()
print(sum(ls))

#count()
print(ls.count(2))

#sort()
lis1=[3535,3534,2343334,634535,2]
lis1.sort()
print(lis1)
lis1.sort(key=None,reverse=True)
print(lis1)
lis1.sort(reverse=True)
print(lis1)

