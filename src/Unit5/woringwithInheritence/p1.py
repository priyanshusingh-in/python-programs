class Parent:
    def __init__(self):
        print('parent')
class Child(Parent()):
    def __init__(self):
        super().__init__(self)
        print('Child')
#print(Parent())
obj=Parent()
obj2=Child()