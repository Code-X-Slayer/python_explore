def under_construction():
    pass

print(under_construction())
# None

print(under_construction)
# <function under_construction at 0x000002AE5D581440>

def say_hello():
    print('hello')
x = 3
for i in range(3):
    say_hello()

# func provide single point if any change needed changing at one pos
# have effect of all usages of it unlike redundancy where each needs modification

def return_hello():
    return 'hello'

return_hello()
# it prints nothing ignored as str comment

x = 3
for i in range(3):
    print(return_hello())

# u only care what ip n op obtained hidde details is abstracted

print(return_hello().upper())

def greet(name):
    print(f'hello, {name}')

greet("corey")
# greet()
# error since arg needed

# we can also have def values
def greet(name = 'world'):
    print(f'hello, {name}')

greet('corey')
greet(name = 'corey')
greet()

# positional arguments
# keyword arguments

# tuple and dict * ie unpacking

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
# ('pos_arg1', 'pos_arg2')
# {'kwarg1': 101, 'kwarg2': 102}

student_info('pos_arg1', 'pos_arg2', kwarg1=101, kwarg2=102)

courses = ['a', 'b', 'c']
info = {'name': 'corey', 'age': 25}
student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year, month):
    if not 1<=month<=12:
        return 'invalid month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(1900))
print(is_leap(2017))
print(is_leap(2020))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))