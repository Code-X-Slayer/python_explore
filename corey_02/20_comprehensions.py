"""lists"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"i want 'n' for each n in nums"
my_list = []
for n in nums:
    my_list.append(n)

my_list = [n for n in nums]

"i want 'n*n' for each n in nums"
my_list = []
for n in nums:
    my_list.append(n**2)

my_list = [n**2 for n in nums]

my_list = map(lambda n : n**2, nums)

"i want 'n' for each n in nums if n is even"
my_list = []
for n in nums:
    if (n&1) == 0:
        my_list.append(n)

my_list = [n for n in nums if (n&1) == 0]

my_list = filter(lambda n : (n&1) == 0, nums)

" i want (letter, num) pair for each letter in 'abcd' and each number in 0123"
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

"""dict"""

names = ['a', 'b', 'c', 'd']
heros = ['A', 'B', 'C', 'D']
# print(zip(names, heros))

'i want a dict{"name" : "hero"} for each name, hero in zip(names, heros)'
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

my_dict = {name : hero for name, hero in zip(names, heros)}

'if name not equals c'
my_dict = {}
for name, hero in zip(names, heros):
    if name!='c':
        my_dict[name] = hero

my_dict = {name : hero for name, hero in zip(names, heros) if name!='c'}

"""sets"""
nums = [1, 1, 2, 3, 3, 4, 5, 5]

my_set = set()
for num in nums:
    my_set.add(num)

my_set = {n for n in nums}

"""Generator expressions"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"i want to yield n*n for each n in nums"

def gen_fun(nums):
    for n in nums:
        yield n*n

my_gen = gen_fun(nums)

my_gen = (n*n for n in nums)

# for i in my_gen:
#     print(i)
