#wap to table

n=int(input("Enter a number: "))
fact=int(input("Print till factor? :"))
if(fact<=20):
    for i in range(1,fact+1):
        print(n, 'x', i, '=', n*i)
else:
    for i in range(1,21):
        print(n, 'x', i, '=', n*i)
    print("Factor limit is only till 20!")