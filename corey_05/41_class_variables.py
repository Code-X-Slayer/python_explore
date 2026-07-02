# we see instance variables for each instant
# assigned by slef keyword those will be set acc for each instant

# now class vraibles are veraibles that r shared across all instances
# inst vraiables unique for each instant but class varmust besame

# now lets say as employees need hike we gonna give
# actually its same for every employee lets see hardcode it

class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp1 = Employee("Corey", 5000)
emp2 = Employee("Schafer", 6000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# as you can see later we need like raise amount for given employee
# we r supposed to add another funcion hradcode there too 0.4*pay
# as you this leads to redudancy and hardcoded once changed say 0.4 to 0.5
# there is no single point of access so multiple corrections needed

class Employee:
    raise_amount = 1.04
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee("Corey", 5000)
emp2 = Employee("Schafer", 6000)

print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

# it seems a little confusing like why we can access class var from both class n instance
# its gonna work like this check for instance if avilable use it
# if not check class class level or any class inherits from

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
# 1.04
# 1.04
# 1.04

print(id(emp1.raise_amount))
print(id(emp2.raise_amount))
print(id(Employee.raise_amount))
# 1280420715760
# 1280420715760
# 1280420715760

# as you can clearly see they r literally accesing from single sourceie class varibales
# to look inot his much use __dict__

print(emp1.__dict__)
# {'name': 'Corey', 'pay': 5000}
print(Employee.__dict__)
# {'__module__': '__main__', '__firstlineno__': 29, 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x0000020E9265D120>, 'apply_raise': <function Employee.apply_raise at 0x0000020E9265D300>, '__static_attributes__': ('name', 'pay'), '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

# now lets see how modifying looks likt
# lets do it using class name

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# 1.04
# 1.04
# 1.04
# 1.05
# 1.05
# 1.05
# as you can see all affected since its affected the single source

emp1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# 1.05
# 1.06
# 1.05
# as you can see only one altered 
# sunce emp1 raise amount created an instance varible now instead affecting class
# this gives us ability to work or having spec value for a spec instnant
# where we wanna have diff value from contant over all instances

# you can check using __dict__
print(emp1.__dict__)
# {'name': 'Corey', 'pay': 5000, 'raise_amount': 1.06}

# so whenever we wanna try to access suhc class vraubles
# use self.class_var since who knows its a spec instnat and had sep value
# so use self. over class_name.
# so we wanna chnage spec inst value use self.
# which gonna override n create a instance varibale for it

# simillarly say we wanted to have single constnt
# then use class_name. so that its not gonna override n provide const for all instances

class Employee:
    c = 0
    def __init__(self, name):
        self.name = name
        Employee.c += 1
    def __del__(self):
        Employee.c -= 1

print(Employee.c)
emp1 = Employee("Corey")
print(Employee.c)
emp1 = Employee("Schafer")
print(Employee.c)

# without __del__ its never gonna dec counter
# 0
# 1 
# 2

# with __del__ its ginna delete and decrease counter
# 0
# 1
# 1