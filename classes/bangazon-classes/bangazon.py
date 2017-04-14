class Department(object):
  """Parent class for all departments"""
  def __init__(self):
      self.employees = {}
      self.office_hours = '9:00-5:00'
      self.contact_info = '123-456-7890'
      self.number_of_employees = 47
      self.manager = "Ned O'neil"
      print(self.manager)

  @property
  def name(self):
    try:
      return self.__name
    except AttributeError:
      return ""

  @name.setter
  def name(self, val):
    if isinstance(val, str):
      raise TypeError('Please provide a string value for the department name')

    if val is not "" and len(val) > 1:
      self.__name = val
    else:
      raise ValueError("Please provide a department name")

  @property
  def manager(self):

    try:
      return self.__manager
    except AttributeError:
      return ""

  @manager.setter
  def manager(self, val):
    if not isinstance(val, str):
      raise TypeError('Please provide a string value for the manager name')

    if val is not "" and len(val) > 5:
      self.__manager = val
    else:
      raise ValueError("Please provide a manager name")
print("Are we running?")

class Marketing(Department):
  
