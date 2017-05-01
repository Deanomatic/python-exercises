class Department(object):
    """Parent class for all departments"""
    def __init__(self, name, contact_info, number_of_employees, manager):
        self.name = name
        self.employees = {}
        self.office_hours = "9:00-5:00"
        self.contact_info = contact_info
        self.number_of_employees = number_of_employees
        self.__manager = manager
        self.meet = ""
        print(name, contact_info, number_of_employees, manager)
    
    def get_budget(self):
        self.budget = '$110,000'
        return self.budget

    @property
    def name(self):
        try:
            return self.name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if isinstance(val, int):
            raise TypeError('Please provide a string value for the department name')

        # if val is not "" and len(val) > 1:
        #     self.name = val
        # else:
        #     raise ValueError("Please provide a department name")

    @property
    def manager(self):

        try:
            return self.__manager
        except AttributeError:
            return ""

    # @manager.setter
    # def manager(self, val):
    #     if not isinstance(val, str):
    #         raise TypeError('Please provide a string value for the manager name')

    #     if val is not "" and len(val) > 5:
    #         self.manager = val
    #     else:
    #         raise ValueError("Please provide a manager name")

Bangazon = Department("Bangazon", "123-123-1231", "25", "Bobby Joe")

print(Bangazon)



