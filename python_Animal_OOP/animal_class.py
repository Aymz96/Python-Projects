# Define our Animal Class.

#sudo
# Looks / Characteristics of every animal
    #  name, age, colour, heart, brain

# Behaviours / Methods of every animal
    #  eat, sleep, reproduce, potty, make_sound

class Animal():
    # define behaviour and characteristics

    # define the characteristics of EVERY animal
    def __init__(self, name, age_days, colour):
        self.name = name
        self.__age_days = age_days
        self.colour = colour
        self.heart = True
        self.brain = True
        self.skills = {}

    # age
    # WE should be able to retrieve the age
    # We SHOULD NOT be able to change / later the age without being an admin
        # A user should not able to se his/her own age
        # however, as the animal sleeps, it should increment the age

    # first let's make the age private
    # create a method that get's the age and returns it
    def get_age(self): # a getter method  - allows access to encapsulated resources
        return self.__age_days #inside the class we have access to the private methods.
    #change the sleep method to increment age

    def set_age(self, age_days):
        # We SHOULD NOT be able to change / alter the age without being an admin

        # fake verification
        password = input('what is the password')

        if password == 'SuperSecrete':
            self.__age_days = age_days
            return True
        else:
            return False


    def eat(self):
        # when it eat it should increment the age
        # we will do this by calling the __increment_age() method
        return 'Nom nom nom'

    # defining the method .eat(), .sleep(), .reproduce(),
    def __increment_age(self):
        self.__age_days += 1


    def sleep(self):
        # incrment age in days by 1
        self.__increment_age()
        return 'zzZZzzzZZzZZ'


    def reproduce(self):
        return "I going to need some privacy here.... :) "

    def potty(self):
        return  "0_0 HUMMM!!! o_0 AHHH!! SPLOSH! o_o "

    def make_sound(self):
        return 'Woof'


# To call methods we need an object of this class

# # # creating an instance of class animal
# ringo = Animal('Ringo', 300, 'bluish') #creates intances of clas animal and assigns to variable ringo
#
# #  me having all access to age_days
# # I can print it
# # print(ringo.age_days)
# #
# # # I can even modify it!
# # ringo.age_days = 'hello'
# # print(ringo.age_days)
#
# print(ringo.get_age())
# print(ringo.set_age(500))
# print(ringo.get_age())

# # checking and print the instance
# print(ringo)
# print(type(ringo))
#
# # calling methods on instance of Animal
# print(ringo.eat())
# print(ringo.potty())
# print(ringo.sleep())
#
# # Check the attribute of an instance
# print(ringo.name)
# print(ringo.age)
#
# # second animal
# mini = Animal('Stacy', 25, 'Goldenish')
# print(mini.age)
# print(mini.colour)