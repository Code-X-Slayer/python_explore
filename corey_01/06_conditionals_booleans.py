if True:
    print("true executing")

if False:
    print("false executing")

lang = 'python'
if lang == "python":
    print('same')

# comparision operators outputs boolean
# < <= > >= == != is

x = int(input("Enter num : "))
if x > 0:
    print('pos')
elif x < 0:
    print('neg')
else:
    print('zero')

# and or not
# all T then and T
# any T then or T
# not inverts 

user = 'admin'
logged_in = True

if user=='admin' and logged_in:
    print('admin page')
else:
    print('bad access')

logged_in = False
if user=='admin' and logged_in:
    print('admin page')
else:
    print('bad access')

logged_in = False
if user=='admin' or logged_in:
    print('admin page')
else:
    print('bad access')

if not logged_in:
    print('logout before exiting')
else:
    print('already logout')

a = [1, 2, 3]
b = [1, 2, 3]

print(a==b) # compare value
print(a is b) # compare memory address

# to check this out use id
print(id(a))
print(id(b))

# if same ref then id will be same
c = a
print(id(a))
print(id(c))

# False values in python
# boolean : False
# numeric : 0
# empty seq or dict : [], (), '', {}, set()
# None

if False:
    print('impossible')

if 0:
    print('impossible')

if [] or () or {} or set():
    print('impossible')

if None:
    print('impossible')

