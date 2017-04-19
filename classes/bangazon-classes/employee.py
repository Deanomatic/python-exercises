import random
from bangazon import Department

class Employees(Department):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@bangazon.com'

    def eat(self, food=None, companions=None):
        """ Method to randomly choose a restaurant with possible variables of food eaten
        and companions.
        """

        restaurant = ["Pie in the Sky", "Famous Dave's", "McDoogal's"]
        self.restaurant = random.choice(restaurant)
        self.food = food
        self.companions = companions

