# special methods enable us to emulate built in behavior

# depending on what obj u r working with addition has diff behavior
print(1+2)
print("a"+"b")

class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('corey', 'schafer', 50000)
# also when we print instance it will print vague employee obj at x address
print(emp1)
# <__main__.Employee object at 0x000002681DFE6F90>

# repr is unambigous representation of objects and be used for debugging and logging
# str is more readable representation of an object to be used as display msg to user

# if we have repr without str then calling str fallback to repr
# usually repr must show str from which we can create another copy 
# we can explicity print repr() and str() in print
# but print() gonna check str() if not then repr() if not then obj at address will b

class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amount)
    def email(self):
        return f"{self.first}-{self.last}.@gmail.com"
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"
    def __str__(self):
        return f"{self.fullname()} - {self.email()}"

emp1 = Employee('corey', 'schafer', 50000)
print(emp1)
print(repr(emp1))
print(str(emp1))
print(emp1.__repr__())
print(emp1.__str__())
# corey schafer - corey-schafer.@gmail.com
# Employee(corey, schafer, 50000)
# corey schafer - corey-schafer.@gmail.com
# Employee(corey, schafer, 50000)
# corey schafer - corey-schafer.@gmail.com

# without str repr str print user repr
# without repr str print uses str whereas repr prints address
# with nothing all falls to address

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))
# 3
# ab
# in this way each class implements its own dunder add
# lets say we wanna do it with our Employee

class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amount)
    def email(self):
        return f"{self.first}-{self.last}.@gmail.com"
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"
    def __str__(self):
        return f"{self.fullname()} - {self.email()}"
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
    
emp1 = Employee('corey', 'schafer', 50000)
emp2 = Employee('test', 'employee', 60000)
# without __add__ if we call emp1+emp2 error
# TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
print(emp1+emp2)
# 110000

# btw len is alos a special method
print(len('test'))
print('test'.__len__())
# 4
# 4

print(len(emp1))
# 13

# btw checkout equality in docs too