class Car:
    def setenginemodel(self,engine):
        self.engine=engine
    def getenginemodel(self):
        print(self.engine)
class Honda(Car):
    def setcarmodel(self,model):
        self.model=model
    def getcarmadel(self):
        print(self.__module__)
mycar=Honda()
mycar.setenginemodel('KE')