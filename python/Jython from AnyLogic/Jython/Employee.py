# Jython source file
from jython_from_al import EmployeeType

class Employee(EmployeeType):
   def __init__(self):
      self.first = "Josh"
      self.last  = "Juneau"
      self.id = "myempid"

   def getEmployeeFirst(self):
      return self.first

   def getEmployeeLast(self):
      return self.last

   def getEmployeeId(self):
      return self.id