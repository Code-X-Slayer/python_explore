def square_numbers(nums):
    res = []
    for num in nums:
        res.append(num**2)
    return res

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)

# its upto normal here so far
# we pass list it calculates sqaures all of them and pass res as list
# lets convert it to generator
def square_numbers(nums):
    for num in nums:
        yield num**2

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)
# its no longer outputting result
# <generator object square_numbers at 0x0000018EBE3FA4D0>

# generators dont hold entire result in memory
# it yields res one by one at a time
# its ready to preoduce next res when asked

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# error ie iterator is exhausted StopIteration means it has no more values
# Traceback (most recent call last):
#   File "O:\tut\corey_04\36_generators.py", line 31, in <module>
#     print(next(my_nums))
#           ~~~~^^^^^^^^^
# StopIteration

# so better use for loop over manual calls
for num in my_nums:
    print(num)

# advantages of generators over lists
# more readable
# converting ist comp to generator is same as replacing [] with ()
nums = [1, 2, 3, 4, 5]
my_nums = [x**2 for x in nums]
my_nums = (x**2 for x in nums)
# if you want all res once and accessable convert back into list
res = list(my_nums)
print(res)
# the main advantage os performance
# because its not storing all values in memory
# this is irrelvant in case of small lists say millions
# so converting back to list will make lose the gainer performance

# lets see a solid exmaple with counts
import random
import time
from memory_profiler import memory_usage
names = ['a', 'b', 'c', 'd', 'e']
majors = ['cse', 'ece', 'aiml', 'ds']
def people_list(num_people):
    res = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        res.append(person)
    return res

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

start_mem = memory_usage()[0]
t1 = time.perf_counter()
people = people_list(100000)
t2 = time.perf_counter()
end_mem = memory_usage()[0]

print(f"Memory (After): {end_mem-start_mem}")
print(f"Took {(t2-t1):.2f}")

start_mem = memory_usage()[0]
t1 = time.perf_counter()
people = people_generator(100000)
t2 = time.perf_counter()
end_mem = memory_usage()[0]

print(f"Memory (After): {end_mem-start_mem}")
print(f"Took {(t2-t1):.2f}")