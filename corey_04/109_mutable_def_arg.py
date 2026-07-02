def add_employee(name, emp_list = []):
    emp_list.append(name)
    print(emp_list)

print(add_employee.__defaults__)
add_employee('Corey1')
print(add_employee.__defaults__)
add_employee('Corey2')
print(add_employee.__defaults__)

# ([],)
# ['Corey1']
# (['Corey1'],)
# ['Corey1', 'Corey2']
# (['Corey1', 'Corey2'],)

# the reason for this for is def values evaluated once when func is created
# ie emp_list is kinf of mapped to [] a specific list at x address
# now u expect it to have to new lists when called
# but since its not gonna happen bcoz def evaluated once
# when 1st call that same mapping [] updated to new one
# and 2nd call too done the same

# now lets see solution
def add_employee_fixed(name, emp_list = None):
    if emp_list is None:
        emp_list = []
    emp_list.append(name)
    print(emp_list)


print(add_employee_fixed.__defaults__)
add_employee_fixed('Corey1')
print(add_employee_fixed.__defaults__)
add_employee_fixed('Corey2')
print(add_employee_fixed.__defaults__)
# (None,)
# ['Corey1']
# (None,)
# ['Corey2']
# (None,)

# now its also same case def args evaluated once
# but in python None is immutable and singleton object
# like emp_list = None at fixed x distance
# now before first call its mapping to None
# at first call now emp_list = [] will create new list with diff address at multiple calls
# the def value is immutable its not gonna change
# like in 1st case too same [] address is carried and so does with 2nd same None obj pointed

# what it really means
# the def args only evaluated once when func created
# it doesnt mean its not gonna set to its def value only one time
# whats the real deal was its gonna point to that was evaluated at for once

# lets see final example
from datetime import datetime
import time

def display_time(time_to_print=datetime.now()):
    print(time_to_print.strftime('%B %d %Y %H %M %S'))

print(display_time.__defaults__)
display_time()
time.sleep(3)
display_time()
# (datetime.datetime(2026, 6, 23, 6, 37, 42, 958644),)
# June 23 2026 06 37 42
# June 23 2026 06 37 42

# as you can see time_to_print evaluated once to the time its went
# and keep on setting to it solution is

def display_time_fixed(time_to_print=None):
    if time_to_print is None:
        time_to_print = datetime.now()
    print(time_to_print.strftime('%B %d %Y %H %M %S'))

print(display_time_fixed.__defaults__)
display_time()
time.sleep(3)
display_time()
# (None,)
# June 23 2026 06 39 26
# June 23 2026 06 39 26