# import all the classes.
from plane_class import Plane
from vehicle_class import Vehicle
from car_class import Car

# create 2 vehicle instances
vehicle1 = Vehicle(10, 15)
vehicle2 = Vehicle(25, 30)

# call methods and attributes to test
print("car accelerateing ")
vehicle1.accelerate()
vehicle2.accelerate()

print("Testing Vehicle breaking - expected result 'Stopping'")
vehicle1.breaking()
vehicle2.breaking()

print("Testing Vehicle with Passengers = 4 and Cargo = 6. Expected result: 4, 3")
print(vehicle1.n_passengers)
print(vehicle1.size_cargo)

print("\nTesting Vehicle with Passengers = 12 and Cargo = 10. Expected result: 12, 10")
print(vehicle2.n_passengers)
print(vehicle2.size_cargo)

# create 2 car instances
# make car accelerate and make them break
# make car honk and park
car1 = Car(4, 6, "Isuzu", 25, 250)
car2 = Car(12, 10, "Tesla", 84, 150)

print("\nTesting Car accelleration")
print(car1.accelerate())
print(car2.accelerate())

print("\nTesting Car breaking")
print(car1.breaking())
print(car2.breaking())

print("\nTesting Car honking")
print(car1.honk())
print(car2.honk())

print("\nTesting Car parking")
print(car1.park())
print(car2.park())

# create 2 plane instances here
# make plane accelerate and make them break
# make plane fly and land

plane1 = Plane(300, 350, "Orange", "UK")
plane2 = Plane(500, 430, "Green", "JPN")

print("\nTesting plane accelleration")
print(plane1.accelerate())
print(plane2.accelerate())

print("\nTesting plane breaking")
print(plane1.breaking())
print(plane2.breaking())

print("\nTesting plane flight")
print(plane1.fly())
print(plane2.fly())

print("\nTesting plane landing")
print(plane1.land())
print(plane2.land())