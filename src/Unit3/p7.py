#wap to find reverse of a number 
def rev(n):

    r=0
    while n>0:
        d=n%10
        r=r*10+d
        n=n//10
    return r
n=int(input())
if rev(n)== n:
    print("Palindrome")
else:
    print("not palindrome")