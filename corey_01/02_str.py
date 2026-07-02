# always use meaningful variable names
message = 'hello world'
m = 'hello world'

# use snake_case mostly in python
my_message = 'hello world'

# single double quotes doesnt matter but use wisely
message = 'bobby\'s view'
message = "bobby's view"

# mutli line string
"""
Can be used as multi line comment
"""

message = 'hello world'

print(message)

# accessing length
print(len(message))

# 0 indexed
print(message[0])
# error since 11 length [0, 10] are valid
# print(message[11]) 


# slicing [a:b] a is inc b is exc
print(message[0:5])
print(message[:5])
print(message[6:])

# str methods
print(message.upper())
print(message.lower())

print(message.count('hello world')) # 1
print(message.count('l')) # 3
print(message.count('a')) # 0

print(message.find('l')) # 2 since first found idx
print(message.find('a')) # -1 since not found

message = 'hello world'
message.replace('world', 'universe')
print(message)
# the same no change since replace method not affect original str
# but returns new modified one whereas python interpreter ignored it since its a str

new_message = message.replace('world', 'universe')
print(new_message)

# if you really want to change original one just re assign it
message = message.replace('world', 'universe')
print(message)

greeting = 'hello'
name = 'corey'
message = greeting + name
print(message) # no space bw 
message = greeting + ", " + name
print(message)

# this seems simple for small but over many req it becomes complex
# use format
message = '{}, {}'.format(greeting, name)
print(message)

# this is aslo much simplied in python versions 3.6 and above ie f strings
message = f"{greeting}, {name}"
print(message)

# dir() shows all attributes and methods that variable has access
print(dir(message))
# __x__ means x is attribute just simply y means a method

# as dir() just mentions what variable can access if we need more info
# use help() but with data type not varaible

# print(help(str))

# if we need more detailed info on a specific one
# print(help(str.lower))