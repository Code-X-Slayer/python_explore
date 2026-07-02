"""
list
"""
# ordered mutable one

courses = ['a', 'b', 'c', 'd']

print(courses)

# index
print(courses[0])
print(courses[-1])
# print(courses[4]) # error

# slicing
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('e')
print(courses)

courses.insert(0, '0')
print(courses)

courses2 = ['1', '2', '3']
courses.insert(1, courses2)
print(courses)
# nested list it is added as list inside our main list

# correct way is to use extend
courses = ['a', 'b', 'c']
courses2 = ['d', 'e', 'f']
courses.extend(courses2)
print(courses)

# to do at certain pos
a = [1, 2]
b = [3, 4]
a[1:1] = b
print(a)

lst = ['a', 'b', 'c', 'd', 'b']

# removes first occurance
lst.remove('b')
print(lst)

# lst.remove('f')
# error since f dont exists

# pop() removes and returns eleat idx mentioned
# if no mentioned by def last idx ele is popped out

lst = [1, 2, 3]
last = lst.pop()
print(f"{lst} -- {last}")
last = lst.pop(-1)
print(f"{lst} -- {last}")

# inplace sort() and reverse() 
nums = [1, 3, 5, 2, 4]
print(nums)
nums.reverse()
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# if you want have sorted version without affecting original one
sorted_nums = sorted(nums)
print(sorted_nums)

# min max
print(max(nums))
print(min(nums))

# like find in str index in list
courses = ['a', 'b', 'c', 'b']
print(courses.index('b'))
# print(courses.index('d'))
# produces error when not exists

# how to safely do first check if exists
if 'd' in courses:
    print(courses.index('d'))
else:
    print(-1)

# looping
courses = ['a', 'b', 'c']
for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(f"{index} : {course}")

for index, course in enumerate(courses, start = 100):
    print(f"{index} : {course}")

# what if we want csv from it
courses_str = ", ".join(courses)
print(courses_str)

# if we want list from csv
courses_list = courses_str.split(', ')
print(courses_list)

"""
tuple
"""
# ordered immutable ones

lst1 = [1, 2, 3]
lst2 = lst1

print(lst1)
print(lst2)

lst2[0] = 100
print(lst1)
print(lst2)

tuple1 = (1, 2, 3)
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple2[0] = 100
# tuples are immutable so its just like lists but only allow ops that dont involve muting

"""
set
"""
# unordered unique

courses = {'b', 'a', 'c', 'a'}

print(courses)
print('b' in courses)
print('d' in courses)

# set ops
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

# empty ones
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()

# this is wrong this will be type of dict
empty_set = {}
print(type({}))
# this is the correct way
empty_set = set()