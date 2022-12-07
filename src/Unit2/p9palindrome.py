#wap to check if a num is palindrome or not
n=int(input("Enter a number: "))
num=n
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
if num==r:
    print("number is palindrome")
else:
    print("number is not palindrome")