unit=int(input())
if(unit>=1 and unit<=100):
    print("Electricity Bill is:",unit*1.5)
elif(unit>=101 and unit<=200):
    print("Electricity Bill is:",unit*2.5)
elif(unit>=201 and unit<=300):
    print("Electricity Bill is:",unit*4)
elif(unit>=300 and unit<=350):
    print("Electricity Bill is:",unit*5)
elif(unit>35):
    print("Electricity Bill is:",unit*15)
else:
    print("Enter correct Unit value!!!")