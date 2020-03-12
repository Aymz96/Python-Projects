from animal_class import *

class Reptile(Animal):

    def __init__(self, name, age, colour, scales, blood_temp):
        super().__init__(name, age, colour)
        self.scales = scales
        self.blood_temp = blood_temp

    def make_sound(self):
        return 'ZLSLSLLSLZLSLLZPHYTHON'


animal1 = Animal('Nacho', 20, 'Yellowish')
reptile1 = Reptile('Ringo', 30, 'yellow', 'lots', 'very cold')

print(animal1)
print(reptile1)

# Reptile has all the attribute and method of Animal
print(reptile1.name) # This is a attribute of reptile not a method


print(reptile1.eat())
print(reptile1.potty())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())