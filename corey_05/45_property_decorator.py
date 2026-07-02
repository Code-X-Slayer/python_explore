# these property decorators enables class attrib to getter setter and deleter 

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"
    def fullname(self):
        return f"{self.first} {self.last}"
    
emp1 = Employee('corey', 'schafer')

print(emp1.email)
# corey.schafer@gmail.com

emp1.first = 'jim'
print(emp1.email)
# corey.schafer@gmail.com
# this is because we constructed email once at object creation
# now we chnage name after constrcution and email not updated
# the solution might be making email as fullnam()
# but all employees need to undergo calculation even no updates

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def fullname(self):
        return f"{self.first} {self.last}"
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
# this needs to update all calls from .email to .email()
# whihc kind of misleading not effective
emp1 = Employee('corey', 'schafer')
emp1.first = 'jim'
print(emp1.email())
# jim.schafer@gmail.com

# property decorator is better solution for this
# as property decorator allows us to define a method
# but we can access it like an attribute
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def fullname(self):
        return f"{self.first} {self.last}"
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

emp1 = Employee('corey', 'schafer')
emp1.first = 'jim'
print(emp1.email)
# jim.schafer@gmail.com

# lets do it with fullname too
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

# btw if we wanna change property value like fullname
# it can lead to error if we change directly
emp1 = Employee('corey', 'schafer')
emp1.first = 'jim'
print(emp1.email)
# emp1.fullname = 'corey schafer'
# AttributeError: property 'fullname' of 'Employee' object has no setter
# as its telling if we wanna modify property value we have setter for it
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

emp1 = Employee('corey', 'schafer')
print(emp1.fullname)
emp1.fullname = 'jim jam'
print(emp1.fullname)
# corey schafer
# jim jam

# deleter
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
emp1 = Employee('corey', 'schafer')
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)
# corey schafer
# Delete name!
# None None