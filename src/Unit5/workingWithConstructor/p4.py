class Student:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
s1_name=input()
s1_age=int(input())
Stud_1=Student(s1_name,s1_age,"arya@gmail.com")
s2_name=input()
s2_age=int(input())
Stud_2=Student(s2_name,s2_age,"rajan@gmail.com")
print('Stud_1.name =',Stud_1.name)
print('Stud_2.name =',Stud_2.name)