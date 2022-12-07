#wap to create a class student with attribute name regno grade display

class student:
    name=None
    regno=None
    grade=None
    def display(self):
        name='Priyanshu Singh'
        regno=12204367
        grade='A+'
        return name,regno,grade
obj1=student()
print(obj1.display())