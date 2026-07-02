li = [3,2,4,5,1]

s_li = sorted(li)
# print(s_li)
# print(li)

li.sort()
# print(li)

# sorted() returns copy of sorted iterable not modifies original
# whereas .sort() returns None but sorts inplace

# ascending order simple .sort()
# sorted(li), li.sort()
# for descending order
# sorted(li, reverse=True), li.sort(reverse=True)

# tuple dont support .sort()
# so we have to use sorted() that too creates new one
# this behaviour is because of immutability

tup = (3,2,4,5,1)
s_tup = sorted(tup)
# sorted list not tuple
# if needed tuple tuple(sorted(tup))
# print(s_tup)
# print(tup)


di = {'name': 'corey', 'job': 'programming', 'age':None, 'os':'Mac'}
# same way .sort() is not available in dict too use sorted()
s_di = sorted(di)
# print(s_di)
# here its just list of keys not values if needed values
sorted_keys = sorted(di.items(), key = lambda item : item[0])
# if needed sort based on values
# sorted_items = sorted(di.items(), key = lambda item: item[1])
# produce error since None exists
# after python 3.7 dict stores insertion order so we can convert obtained sorted list back to dict
# s_di = dict(sorted(di.items(), key = lambda item : item[1]))


# sorting based on custom logic
# this can be done by passing key param the required logic

li = [-6, -5, -4, 1, 2, 3]
# wanted sort based on abs value
s_li = sorted(li, key=abs)
# print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.age}, ${self.salary}'
    
e1 = Employee("a", 30, 30000)
e2 = Employee("b", 40, 40000)
e3 = Employee("c", 50, 50000)

employees = [e1, e2, e3]

# this line produces error since interpreter dont know how to sort these objects
# s_employees = sorted(employees)

# earier abs, len all are built-in so we have to write our custom logic
def sort_name(emp):
    return emp.name

def sort_age(emp):
    return emp.age

def sort_salary(emp):
    return emp.salary

print(sorted(employees, key=sort_name))
print(sorted(employees, key=sort_age))
print(sorted(employees, key=sort_salary))
print(sorted(employees, key=sort_salary, reverse=True))
print(sorted(employees, key=lambda emp : emp.salary, reverse=True))

from operator import attrgetter
print(sorted(employees, key=attrgetter('salary'), reverse=True))