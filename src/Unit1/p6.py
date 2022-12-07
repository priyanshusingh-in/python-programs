#Wap to to input name percentage age and mobile number and print using normal print method and using .format() with placeholders

name=(input("Enter name: "))
percentage=float(input("Enter percentage: "))
age=int(input("Enter age: "))
mobileNumber=int(input("Enter Mobile Number:"))

print("The name of student is {}, his percentage is {}. His age is {} and his mobile number is {}".format(name,percentage,age,mobileNumber))