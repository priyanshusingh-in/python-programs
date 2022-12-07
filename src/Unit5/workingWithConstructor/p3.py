class Car:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
Honda=Car()
carname=input()
Honda.setName(carname)
print(Honda.getName())