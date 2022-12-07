class Car:
    name=None
    color=None
    def get_Speed(self):
        name='Honda City'
        color='Red'
        return name+' is available in '+color+'color'
Honda=Car()
print(Honda.get_Speed())