class Car:
    def __init__(self, name, brand, color, maxSpeed, numberPlate):
        self.name = name
        self.brand = brand
        self.color = color
        self.maxSpeed = maxSpeed
        self.numberPlate = numberPlate

    def changeColor(self,newColor):
        self.color = newColor

    def getStats(self):
        print(self.name)
        print(self.brand)
        print(self.color)
        print(self.maxSpeed)
        print(self.numberPlate)

        
Car1 = Car("Nexa", "Maruti", "Blue", "80Kmph", "KA31JO3378" )
Car2 = Car("Bullet", "Gun", "black", "100Kmph", "KA09PL9987")

Car1.changeColor("Red")

Car1.getStats()
Car2.getStats()