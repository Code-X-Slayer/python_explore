"""
LEGB
Local, Enclosing, Global, Built-in
"""

# x = 'global x'

# def test():
#     y = 'local y'
#     # print(y) # local y
#     print(x) # global x

# test()

# def test():
#     x = 'local x'
#     print(x)

# test() # local x
# print(x) # global x

# def test():
#     global x
#     x = 'local x'
#     print(x)

# test() # local x
# print(x) # local x

# def test():
#     global z
#     # without this print(z) outside func will produce error
#     z = 'local z'
#     print(z)

# test()
# print(z)

# z = 'global z'

# def test(z):
#     z = z.upper()
#     print(z)

# test('local z')
# just same as local variables
# print(z) produces global z

# this behaviour is python to provide isolated local scope
# which prevents us accidentally chosing broader scope varaibles

# built in scope
# import builtins
# print(dir(builtins))
# errors n built in functions like len, max, min etc
# python make us to not use them if we use produce error

# print(min([1,2,3]))

# def min():
#     pass

# no errors till here
# print(min([1,2,3]))
# min() takes 0 positional arguments but 1 was given
# ie min builtin was overided by our custom function
# fell to scope over builtin (dont ever do it)

# x = 'global x'

# def outer():
#     # x = 'outer x'
#     def inner():
#         # x = 'inner x'
#         print(x)
#     inner()
#     print(x)

# outer()
# op without commenting any is inner and outer
# op with  just commenting inner x is outer and outer
# op with just commenting outer x is inner and global
# op with commenting both inner n outer x is global

# global keyword using inside inner() affects diertly global x
# x = 'global x'

# def outer():
#     def inner():
#         global x
#         x = 'inner x'
#     inner()

# outer()
# print(x)

# in order to access just the above use nonlocal
# nonlocal requires variable created
x = 'global x'

def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        print(x)
        x = 'inner x'
    inner()
    print(x)

outer()
print(x)