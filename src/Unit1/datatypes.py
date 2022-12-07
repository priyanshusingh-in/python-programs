a=False

#List
x=[1,24.4,"hello", True, a]
print(type(x))
print(x)
print(x[2])
print(x[-2])

#String
S="apple"
print(S)

#Tuples
t=(345,35.535,355+34j,True,a)
print(t)

#Sets
set={2,2,2,534.52,2,4,2,"Hello",'Hello',534.52}
print(set)

#Dictionary
Dict={1:34,2:"Hello World",3:True,'ab':344+354j}
print(Dict)
print(Dict['ab'])
print(type(Dict))
print(Dict.get(2))