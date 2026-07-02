# Duck typing and easier to ask forgiveness than permission (EAFP)

class Duck:
    def quack(self):
        print("Quack Quack")
    
    def fly(self):
        print("Flap Flap")

class Person:
    def quack(self):
        print("I'm quacking like duck")

    def fly(self):
        print("I'm flapping my arms")


# non ducktyping way is to check instance and calling
def quack_and_fly(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("Thing has to be a Duck")

quack_and_fly(Duck())
# Quack Quack
# Flap Flap
quack_and_fly(Person())
# Thing has to be a 

# whereas ducktyping tells if a thing does quack and fly then consider it as duck
# so as long as a thing implements required to duck its a duck
def quack_and_fly(thing):
    thing.quack()
    thing.fly()

# now person also considered as duck here
quack_and_fly(Duck())
# Quack Quack
# Flap Flap
quack_and_fly(Person())
# I'm quacking like duck
# I'm flapping my arms

# now this comes with caution 
# what if passed thing dont has those methods it will be in danger
# so the concpet is its easier to ask forgiveness than permission

# lets solve this
# 1st non pythonic way Look Before You Leap
def quack_and_fly(thing):
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# 2nd pythonic way ask forgiveness like call it
# if not exists handle error'
def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# another example
person = {'name': 'Corey', 'age': 30, 'job': 'programmer'}
person = {'name': 'Corey', 'age': 30}

# non pythonic way (LBYL)
if 'name' in person and 'age' in person and 'job'in person:
    print(f"Name: {person['name']}, Age: {person['age']}, Job: {person['job']}")
else:
    print("Missing some keys")

# pythonic way (EAFP)
try:
    print(f"Name: {person['name']}, Age: {person['age']}, Job: {person['job']}")
except KeyError as e:
    print(f"Missing key {e}")

# another exmample
lst = [1, 2, 3, 4, 5]

# non pythonic (LBYL)
if len(lst) >= 6:
    print(lst[5])
else:
    print('That index doesnt exists')

# pythonic (EAFP)
try:
    print(lst[5])
except IndexError as e:
    print('That index doesnt exist')

# example from docs
import os
my_file = "test.txt"

# non pythonic way leads to race conditions
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File cant be accessed')

# pythonic way no race condition
try:
    f = open(my_file)
except IOError as e:
    print('file cant be accessed')
else:
    with f:
        print(f.read())
