person = {'name': 'corey', 'age': 23}

sentence = "My name is " + person['name'] + " and my age is " + str(person['age'])

sentence = "My name is {} and my age is {}".format(person['name'], person['age'])

sentence = "My name is {0} and my age is {1}".format(person['name'], person['age'])

tag = 'h1'
text = 'headline1'
sentence = "<{0}>{1}</{0}>".format(tag, text)

sentence  = "My name is {0[name]} and my age is {0[age]}".format(person)

lst = ['coery', 23]
sentence  = "My name is {0[0]} and my age is {0[1]}".format(lst)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('corey', 23)
sentence  = "My name is {0.name} and my age is {0.age}".format(person)

sentence = "My name is {name} and my age is {age}".format(name='corey', age=30)

person = {'name': 'corey', 'age': 30}
sentence = "My name is {name} and my age is {age}".format(**person)

for i in range(3):
    print("{}".format(i))

for i in range(3):
    print("{:02}".format(i))

pi = 3.141592
print("pie is {:.3f}".format(pi))

sentence = "1mb is {:,} bytes".format(1024**2)
print(sentence)

sentence = "109.109 square is {:,.3f}".format(109.109**2)
print(sentence)

import datetime
my_date = datetime.datetime(2026, 6, 19, 13, 54, 42)

print(my_date)

sentence = "{:%B %d, %Y}".format(my_date)
print(sentence)

sentence = "{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year".format(my_date)
print(sentence)