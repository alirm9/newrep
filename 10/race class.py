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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.name} Status ---")
        print(f"{'Reg Num':<10} | {'Max Speed (km/h)':<18} | {'Current Speed (km/h)':<20} | {'Distance (km)':<15}")
        print("-" * 72)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.maximum_speed:<18} | {car.current_speed:<20} | {car.travelled_distance:<15.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

# Main program setup
participating_cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Demolition Derby", 8000, participating_cars)

hours_elapsed = 0
while not race.race_finished():
    race.hour_passes()
    hours_elapsed += 1
    
    if hours_elapsed % 10 == 0:
        print(f"\n[Hour {hours_elapsed}]")
        race.print_status()

# Print final status when the race ends
print(f"\n=== RACE FINISHED IN {hours_elapsed} HOURS ===")
race.print_status()