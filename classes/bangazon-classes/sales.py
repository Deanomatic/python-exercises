from bangazon import Department

class sales(Department):
    def __init__(self, contact_info, number_of_employees, manager):
        super(sales).__init__(contact_info, number_of_employees, manager).get_budget()
        self.contact_info = "123-321-4312"
        self.number_of_employees = "17"
        self.manager = "Wanda Ling"
        self.dep_name = "Sales"
    
    def get_budget(self):
        self.budget += '$5,000'
        return self.budget

Sales = sales()