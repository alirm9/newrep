class Dog:
    def __init__(self, name, breed, sound="Woof"):
        self.name = name
        self.breed = breed
        self.sound = sound
    def bark(self,tiems=1):
        for i in range(tiems):
            print(self.sound)
        return
dog1 = Dog("Buddy", "Shepherd")
dog2 = Dog("Max", "Labrador", "Bark")
print(f"Dog's name: {dog1.name}, Breed: {dog1.breed}, Sound: {dog1.sound}")
print(f"Dog's name: {dog2.name}, Breed: {dog2.breed}, Sound: {dog2.sound}")
dog1.bark(1)
dog2.bark(2)