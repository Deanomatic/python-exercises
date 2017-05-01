######################
# Animal
######################
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0
    def getName(self):
        return self.name

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def setSpecies(self, species):
        self.species = species

    def getSpecies(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "{} is a {}".format(self.name, self.species)

######################
# IsClawed
######################

class IsClawed:
    def __init__(self, retractable=False):
        self.claws = True
        self.claws_are_rectractable = retractable

######################
# IsWhiskered
######################

class IsWhiskered:
    def __init__(self):
        self.whiskers = True
        self.whiskers_count = 0

    # NOTE: IsWhiskered() is the constructor function. If we want it used
    # NOTE: in anything else. We have to pass it in (See Cat && Dog Below)


    def loseWhisker(self, count):
        # NOTE: loseWhisker is a method of a class
        self.whiskers_count -= count 

######################
# Cat
######################

class Cat(Animal, IsWhiskered, IsClawed):
    def __init__(self, name):
        # NOTE: __init__ is the constructor function
        Animal.__init__(self, name, "Cat")
        IsWhiskered.__init__(self)
        IsClawed.__init__(self)
        self.retractable = True
    print("Cat constructor")

    def walk(self):
        self.speed = self.speed + (0.25 * self.legs)

######################
# Dog
###################### 

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
            # NOTE: class Dog() does not get the def __init__(line 2) of class Animal
            # NOTE: to get this. We run line 27 (Animal.__init__(self, name, "Dog"))
            # NOTE:

    def walk(self, speed):
        self.speed = self.speed + (0.2 * self.legs)

######################
# Cat
######################



fido = Dog('Fido')
print(fido)
tommy = Animal('Tommy', 'Tortoise')
print(tommy)
jerry = Cat('Jerry')
print(jerry)