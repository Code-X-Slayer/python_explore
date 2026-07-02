first_name = 'corey'
last_name = 'schafer'

sentence = "My name is {} {}".format(first_name, last_name)
sentence = f"My name is {first_name.upper()} {last_name.upper()}"

person = {'name' : 'corey', 'age': 30}
sentence = "My name is {} and I am {} years old".format(person['name'], person['age'])
sentence = f"My name is {person['name']} and I am {person['age']} years old"

calculation = f"4 times 11 is equals {4*11}"

n = 5
for i in range(n):
    table = f"{n} X {i} = {n*i}"

pi = 3.141592
sentence = f"PI equals: {pi:.3f}"

import datetime
birthday = datetime.datetime(2007, 7, 13)
sentence = f"Birthday was {birthday:%B %d %Y}"
print(sentence)