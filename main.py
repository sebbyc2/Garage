class Vehicle:
    
    def __init__(self, colour, condition):
        self.colour = colour
        self.condition = condition

class Garage:

    garageContents = []

    def __init__(self, name):
        self.name = name
    
    def addVehicle(self, Vehicle):
        Garage.garageContents.append(Vehicle)

    def removeVehicle(self, Vehicle):
        Garage.garageContents.remove(Vehicle)

    def fixVehicle(self, Vehicle):
        cost: 100
        if Vehicle.condition == "A":
            print("Repair cost: £" + (cost * 0.5))
        if Vehicle.condition == "B":
            print("Repair cost: £" + cost)
            Vehicle.condition = "A"
        if Vehicle.condition == "C":
            print("Repair cost: £" + (cost * 1.5))
            Vehicle.condition = "A"

class Car(Vehicle):
    def __init__(self, colour, condition, make, age):
        self.colour = colour
        self.condition = condition
        self.make = make
        self.age = age
        self.wheels = 4

class Boat(Vehicle):
    def __init__(self, colour, condition, make, age):
        self.colour = colour
        self.condition = condition
        self.make = make
        self.age = age
        self.wheels = 0

class Motorbike(Vehicle):
    def __init__(self, colour, condition, make, age):
        self.colour = colour
        self.condition = condition
        self.make = make
        self.age = age
        self.wheels = 2
garage1 = Garage("Wheeler Dealer")
car1 = Car("Blue", "A", "bmw", 8)
garage1.addVehicle(car1)
print(car1)

