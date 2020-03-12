from vehicle_class import Vehicle
# create 2 vehicle instances

# call methods and attributes to test

# create 2 car instances
# make car accelerate and make them break
# make car honk and park

# create 2 plane instances here
# make plane accelerate and make them break
# make plane fly and land

class Plane(Vehicle):
    def __init__(self, n_passengers, cargo_size, colour, country):
        super().__init__(n_passengers, cargo_size)
        self.colour = colour
        self.country = country


    def fly(self):
        return 'Lets Flying'

    def land(self):
        return 'We are Landing'

