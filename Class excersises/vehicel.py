class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class SportsItem:
    def __init__(self, weight):
        self.weight = weight

class Bicycle(Vehicle, SportsItem):
    def __init__(self, speed, weight, gears):
        Vehicle.__init__(self, speed)
        SportsItem.__init__(self, weight)

        self.gears = gears

b = Bicycle(45, 18.7, 3)
print(b.gears)
print(b.speed)
print(b.weight)