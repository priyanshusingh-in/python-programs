#wap to check if the year entered by the user is the leap year or not
year=int(input("Enter leap year: "))
if((year%400==0) or (year%4==0 and year%100!=0)):
    print("It is a leap year!")
else:
    print("It is not a leap year!")