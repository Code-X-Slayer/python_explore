# context managers in python allow us to manage resources
# so we can set up whats exactly what wanted 

f = open('test.txt')
print(f.read())
f.close()

# lets see context manager way of doing using `with`
# this helps us handle errors n safely close in case error
# or else upon complete execution automatically
with open('test.txt') as f:
    print(f.read())

# there are so many plenty use cases of them like
# opening n closing db connections
# acquiring and releasing locks

# we can make create our own in 2 ways
# by using a class or by using a function with decorator

class Open_File():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc, tb):
        self.file.close()

with Open_File('test.txt', 'r') as f:
    print(f.read())

# with Open_File('test.txt', 'r') its just call init
# its initiazes it variables to given parameters
# then with goonna call enter method
# so enter method gonna open file and return it
# so f in above line was return value of enter method
# so f is file object inside our context manager
# and finally at case of error or else execution of whole block
# exit method will be called which closes file for us

# lets see with function for this we need contextlib module
# ie to import context manager decorator
from contextlib import contextmanager

# we use this contextmanager decorator to decorate a generator dunction

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file('test.txt', 'r') as f:
    print(f.read())

# its the same as equaivalent as above class with less code
# above yield its like init and after yield its like exit
# making it open file in init and close file in exit
# and let with block use file object

# btw unlike class we need to explicity handle errors so
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

# lets see a real example
import os

cwd = os.getcwd()
os.chdir('folder1')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('folder2')
print(os.listdir())
os.chdir(cwd)

# lets see here setting up is like storing cwd and chdir to given
# and yield gonna sep it and finally we need to rechnage ot back to cwd

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('folder1'):
    print(os.listdir())

with change_dir('folder2'):
    print(os.listdir())