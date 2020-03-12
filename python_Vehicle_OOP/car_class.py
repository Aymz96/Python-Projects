from vehicle_class import Vehicle

# Define car class here and make it inherit from vehicle

class Car(Vehicle):
    def __init__(self, n_passengers, cargo_size, brand, horse_power, max_speed):
        super().__init__(n_passengers, cargo_size)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed

    def park(self):
        return "PARKING INTO AVAIILABLE "

    def honk(self):
        return "BEEEEEEEEEP!!!"


#Characterists:
# brand
# horse_power
# max_speed

#methods :
# park
# honk

