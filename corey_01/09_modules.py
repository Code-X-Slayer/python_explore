import sys
print(sys.path)

# if you wanna import modules from another folder
# worst thing to do is append manually in ech script
# sys.path.append(/path/to/module)

# which is not ec so add it to env variables so that it can be accessible

from my_module import find_index
import my_module
# this doesnt pollute namesapce
# import my_module as mm
# this does
# from my_module import *

courses = ['a', 'b', 'c', 'd']

# index = mm.find_index(courses, 'b')
index = find_index(courses, 'b')
print(index)

# if we just import only func we cant able to access test var
# but in earlier version whole import we can access

import math

rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2022))

import os
print(os.getcwd())

# all modules r python scripts that were written to not reinvent wheel
# to find out its location use dunder file
print(os.__file__)
print(my_module.__file__)

import antigravity