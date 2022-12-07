w=float(input("Enter weight in pounds: "))
h=float(input("Enter height in inches: "))
weightInKG=w*0.45359237
heightInM=h*0.0254
bmi=weightInKG/(pow(heightInM,2))

if(bmi<18.5):
    print("Underweight")
if(bmi<25):
    print("Normal")
if(bmi<30):
    print("Overweight")
else:
    print("Obese")
