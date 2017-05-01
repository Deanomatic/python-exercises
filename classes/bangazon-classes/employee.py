import random
from bangazon import Department 

class Employees(Department):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@bangazon.com'

    # def eat(self, food=None, companions=None):
    #     """ Method to randomly choose a restaurant with possible variables of food eaten
    #     and companions.
    #     """
    #     restaurant = ["Pie in the Sky", "Famous Dave's", "McDoogal's"]
    #     self.restaurant = random.choice(restaurant)
    #     self.food = food
    #     self.companions = companions
def eat(self, food=None, companions=None):
		resturant_list = ["Chili's", "Red Robin", "Marsh House"]
		random_resturant = resturant_list[random.randrange(3)]

		if food is not None and companions is not None:
			print("{} {} ate a/some {} at {} with {}".format(self.first_name, self.last_name, food, random_resturant, (', '.join(companions))))			
		elif food is not None and companions is None:
			print("{} {} ate a/some {} at the office".format(self.first_name, self.last_name, food))
		elif companions is not None:
			print("{} {} ate at {} with {}".format(self.first_name, self.last_name, random_resturant, (', '.join(companions))))
		else:
			print("{} {} ate at {}".format(self.first_name, self.last_name, random_resturant))
			return random_resturant

rick = Employees("Rick", "Smith")
rick.eat()
print(rick.first_name + " " +  rick.last_name  + " " + rick.email)