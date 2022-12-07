#wap to check if student is eligible to watch or not

from xmlrpc.client import boolean


age=int(input("Enter age: "))
vc=bool(input("Do you have voter card?: "))
S=bool(input("Are you enrolled in any course?: "))

if(age>=18 and vc==True or S==True):
    print("YOU ARE ELIGIBLE!")
else:
    print("SORRY, YOU ARE NOT ELIGIBLE!")