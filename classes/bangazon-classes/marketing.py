from bangazon import Department

class Marketing(Department):
    def __init__(self, name, contact_info, number_of_employees, manager, meeting):
        super().__init__(name, contact_info, number_of_employees, manager)
        self.name = name
        self.contact_info = contact_info
        self.number_of_employees = number_of_employees
        self.__manager = manager
        self.meeting = meeting
        #print(self.contact_info, self.manager, self.number_of_employees, "Break room")
    
    def get_budget(self):
        self.budget = super().get_budget() + '$30,000'
        return self.budget
        print(self.budget)

if __name__ =='__main__':
    marketing = Marketing("Marketing", "098-765-4321", "13", "Ned Schneebly", "Break room")

print(marketing)
