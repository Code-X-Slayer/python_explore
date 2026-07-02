# inheritance
# sub classes inherit methods n attrib from parent class

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    pass

dev1 = Employee('corey', 'schafer', 50000)
dev2 = Employee('test', 'employee', 60000)

print(dev1.email)
print(dev2.email)

dev1 = Developer('corey', 'schafer', 50000)
dev2 = Developer('test', 'employee', 60000)

print(dev1.email)
print(dev2.email)

# print(help(Developer))
# class Developer(Employee)
#  |  Developer(first, last, pay)
#  |
#  |  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object                                                                                 
#  |                                                                                                      
#  |  Methods inherited from Employee:                                                                    
#  |                                                                                                      
#  |  __init__(self, first, last, pay)                                                                    
#  |      Initialize self.  See help(type(self)) for accurate signature.                                  
#  |                                                                                                      
#  |  apply_raise(self)                                                                                   
#  |                                                                                                      
#  |  fullname(self)                                                                                      
#  |                                                                                                      
#  |  ----------------------------------------------------------------------                              
#  |  Data descriptors inherited from Employee:                                                           
#  |                                                                                                      
#  |  __dict__                                                                                            
#  |      dictionary for instance variables                                                               
#  |                                                                                                      
#  |  __weakref__                                                                                         
#  |      list of weak references to the object                                                           
#  |                                                                                                      
#  |  ----------------------------------------------------------------------                              
#  |  Data and other attributes inherited from Employee:                                                  
#  |                                                                                                      
#  |  raise_amount = 1.04 

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
# 50000
# 52000

# now lets change only dev raise it doesnt affect employee

class Developer(Employee):
    raise_amount = 1.10

emp1 = Employee('Corey', 'Schafer', 50000)
dev1 = Developer('Corey', 'Schafer', 50000)
print(emp1.pay)
print(dev1.pay)
emp1.apply_raise()
dev1.apply_raise()
print(emp1.pay)
print(dev1.pay)
# 50000
# 50000
# 52000
# 55000

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev1 = Developer('Corey', 'Schafer', 50000, 'python')
print(dev1.raise_amount)
print(dev1.prog_lang)
# 1.1
# python

# lets test another better subclass
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # Employee.__init__(first, last, pay)
        super().__init__(first, last, pay)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}")
    
mgr_1 = Manager('sue', 'smith', 90000, [dev1])
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev2)
mgr_1.print_emps()
mgr_1.rem_emp(dev1)
mgr_1.print_emps()

# final two imp methods isinstance and issubclass
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
# True
# True
# False
print(issubclass(Manager, Employee))
print(issubclass(Manager, Manager))
print(issubclass(Manager, Developer))
# True
# True
# False