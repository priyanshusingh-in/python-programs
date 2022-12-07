s1=int(input("enter side 1: "))
s2=int(input("enter side 2: "))
s3=int(input("enter side 3: "))
if(s1==s2 and s1==s3):
    print("Triangle is equilateral")
elif(s1==s2 or s1==s3):
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")