weight1=int(input("Enter Weight for package 1: "))
price1=int(input("Enter price for package 1: "))
weight2=int(input("Enter Weight for package 2: "))
price2=int(input("Enter price for package 2: "))
if(weight1*price1<weight2*price2):
    print("Package 1 has the better price.")
else:
    print("Package 2 has the better price.")