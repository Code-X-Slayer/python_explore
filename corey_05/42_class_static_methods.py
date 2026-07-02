# regular methods vs class methods
# regular methods in class automatically take the instance as a first argument and we call it self
# no to change it from instance to taking class as first arg to do that we nee dclass methods
# to convert reg to class methods is as simple as adding a decorator

class Employee:
    c = 0
    raise_amount = 1.04

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp1 = Employee("Corey", 5000)
emp2 = Employee("Schafer", 6000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# 1.04
# 1.04
# 1.04

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# 1.05
# 1.05
# 1.05

Employee.set_raise_amount(1.06)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# 1.06
# 1.06
# 1.06

emp1.set_raise_amount(1.07)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# 1.07
# 1.07
# 1.07

# alternative constructors
# given str to construct another one
    
class Employee:
    c = 0
    raise_amount = 1.04

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        name, pay = emp_str.split('-')
        return cls(name, pay)
    
emp_str = 'Corey-5000'
name, pay = emp_str.split('-')
emp3 = Employee(name, pay)
print(emp3.name, emp3.pay)
emp3 = Employee.from_string(emp_str)
print(emp3.name, emp3.pay)

# now lets see static methods these r diff from class methods
# regular methods automatically pass instance as first arg we call it self
# class methods automatically pass class as first arg we call it cls
# static methods dont pass anything automatically they dont pass inst or cls
# so thye behave like regular functions except they include in classes 
# we usually group them with class since tehy have logical connection
# so simply if u dnt access inst or cls its static @staticmethod

class Employee:
    c = 0
    raise_amount = 1.04

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        name, pay = emp_str.split('-')
        return cls(name, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
import datetime
friday = datetime.date(2026, 6, 26)
saturday = datetime.date(2026, 6, 27)
print(Employee.is_workday(friday))
print(Employee.is_workday(saturday))
# True
# False