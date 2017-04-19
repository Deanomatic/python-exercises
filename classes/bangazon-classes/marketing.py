from bangazon import Department

class marketing(Department):
    def __init__(self, contact_info, number_of_employees, manager, meeting):
        Department.__init__(contact_info, number_of_employees, manager)
        super(marketing, self).get_budget()
        self.contact_info = "777-888-9999"
        self.manager = "Ned O'Neil"
        self.number_of_employees = 13
        self.meeting = meeting
        print(self.contact_info, self.manager, self.number_of_employees, "Break room")
    
    def get_budget(self):
        self.budget -= '$30,000'
        return self.budget


Marketing = marketing("123-123-1234", "13", "Ned Schneebly", "Break room")

print(Marketing)