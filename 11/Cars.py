class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

# Main program
ev = ElectricCar("ABC-15", 180, 52.5)
gas_car = GasolineCar("ACD-123", 165, 32.3)

# Select speeds for both cars
ev.current_speed = 110
gas_car.current_speed = 95

# Drive for 3 hours
ev.drive(3)
gas_car.drive(3)

# Print out the values of their kilometer counters
print(f"Electric car ({ev.registration_number}) odometer: {ev.travelled_distance} km")
print(f"Gasoline car ({gas_car.registration_number}) odometer: {gas_car.travelled_distance} km")