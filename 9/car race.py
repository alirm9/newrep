import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# Main program setup
cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_num, max_speed))

# Race loop
race_ongoing = True
while race_ongoing:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_ongoing = False

# Print results formatted into a table
print(f"{'Reg Num':<10} | {'Max Speed (km/h)':<18} | {'Current Speed (km/h)':<20} | {'Distance (km)':<15}")
print("-" * 72)
for car in cars:
    print(f"{car.registration_number:<10} | {car.maximum_speed:<18} | {car.current_speed:<20} | {car.travelled_distance:<15.1f}")