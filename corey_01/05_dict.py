student = {'name' : 'abc', 'age' : 25, 1: 101}

print(student)
print(student['name'])
print(student[1])
# print(student[101]) 
# error while accessing non existing ones

# use get method for safety return None
print(student.get('name'))
print(student.get('phone'))

# we can also make it return custom value if not exists
print(student.get('phone', 'Not Exists'))

# adding or updating
student['phone'] = '555-555-5555'
student['name'] = 'def'
print(student)
# {'name': 'def', 'age': 25, 1: 101, 'phone': '555-555-5555'}

student.update({'name' : 'ghi', 'age': 35, 'address': 'have to find'})
print(student)

del student['address']
print(student)

age = student.pop('age')
print(age)

# del student['xyz']
# student.pop('xyz')
# error to safe use check

if 'xyz' in student:
    print(student['xyz'])
else:
    print("Not found such key")

print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(f"{key} -> {value}")