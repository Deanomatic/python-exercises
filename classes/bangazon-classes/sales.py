from bangazon import Department

class Sales(Department): 
    def __init__(self, name, contact_info, number_of_employees, manager):

        super().__init__(name, contact_info, number_of_employees, manager)
        self.name = name
        self.contact_info = contact_info
        self.number_of_employees = number_of_employees
        self.__manager = manager
    
    def get_budget(self):
        self.budget += '$5,000'
        return self.budget

new_sales = Sales("Sales", "345-747-0987", "4", "Hector Jonson")

print(new_sales)`