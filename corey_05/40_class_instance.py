# attributes and methods
# class is blueprint for creating instances
# objects were those instances all them r diff

class Employee:
    pass

# emp1 = Employee()
# emp2 = Employee()
# print(emp1)
# print(emp2)
# <__main__.Employee object at 0x000001A1B9866F90>
# <__main__.Employee object at 0x000001A1B9BF4B90>

# instance variables
# contains data unique to each instance
# we can create instance variables for each employee
# by doing following

emp1 = Employee()
emp1.first = 'corey'
emp1.pay = 5000

emp2 = Employee()
emp2.first = 'schafer'
emp2.pay = 6000

# print(emp1.first, emp1.pay)
# print(emp2.first, emp2.pay)
# corey 5000
# schafer 6000

# now its lot of code and manual setup
# special init method to make better use of classes
# whenever we create a method in class 
# they recieve the instance as first argument
# by convention we use self

class Employee:
    def __init__(self, first, pay):
        self.first = first
        self.pay = pay

emp1 = Employee('corey', 5000)
emp2 = Employee('schafer', 6000)
# print(emp1.first, emp1.pay)
# print(emp2.first, emp2.pay)
# corey 5000
# schafer 6000

# as we call Employee('corey', 5000)
# emp1 will be passed as self and first, pay acc

# lets have a sample method
class Employee:
    def __init__(self, first, pay):
        self.first = first
        self.pay = pay
    def test(self):
        return f"{self.first} - {self.pay} /-"

emp1 = Employee('corey', 5000)
emp2 = Employee('schafer', 6000)
print(emp1.test())
print(emp2.test())

# corey - 5000 /-
# schafer - 6000 /-

# lets miss self in method n see what happens
# class Employee:
#     def __init__(self, first, pay):
#         self.first = first
#         self.pay = pay
#     def test():
#         return f"{self.first} - {self.pay} /-"

# print(Employee('coreyschafer', 1000).test())
# TypeError: Employee.test() takes 0 positional arguments but 1 was given
# as u can self ie obj is automatically passing
# where as test() expect no arg we r getting 1 arg

# we can also do same thing in another way
# print(emp1.test())
# print(Employee.test(emp1))
# corey - 5000 /-
# corey - 5000 /-