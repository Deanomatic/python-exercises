class Company():
    """This represents a company in which people work"""

    def __init__(self, name, employees):
        self.name = name
        self.employees = list()

    def hire_employees():
        pass


    def get_name(self):
        """Returns the name of the company"""
        return self.name

class Employee():
    def __init__(self, name, salary, title, start_date):
        self.name = name
        self.salary = salary
        self.title = title
        self.start_date = start_date
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

dean = Employee("Dean", "$100,000", "Manager", "Today")
will = Employee("Will", "$1,000", "Lil Dev", "soon")
jessica = Employee("Jessica", "$$$", "Lil Dev", "soon")

print(dean.name + " makes " + dean.salary + " as a company " + dean.title)
print(will.name + " makes " + will.salary + " as a company " + will.title)
print(jessica.name + " makes " + jessica.salary + " as a company " + jessica.title)
good_company = Company("Good Company", dean)

print(Employee)

