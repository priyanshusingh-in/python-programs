#wap to find factorial of a user input number

n=int(input("Enter a number to find factorial: "))
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("The factorial is : ",fact)
