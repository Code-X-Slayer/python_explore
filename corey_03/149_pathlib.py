import os
from pathlib import Path

# Old: inside project build paths like this os.path.join(BASE_DIR, 'subdir')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# NewL inside project build paths like this BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# prints current working directory
# print(Path.cwd())
# O:\tut\corey_03

# Path() with no params is default is curr directory
# # iterdir() iterates the path ie current directory
# for path in Path().iterdir():
#     print(path)
# 149_pathlib.py
# test_file.txt
# Directory_1

# we r creating new Path objects
# we r passing relative path as from working directory
my_dir = Path("Directory_1")
my_file = Path("file1.txt")
# new_file = my_dir / "new_file.txt"
new_file = my_dir.joinpath("new_file.txt")

# while just passing obj prints relative path
# print(my_dir)
# print(my_file)
# print(new_file)
# Directory_1
# file1.txt
# Directory_1\new_file.txt

# while .name is used for explicilty for file/dir with no extra path
# it gives its name + extension 
# print(my_dir.name)
# print(my_file.name)
# print(new_file.name)
# Directory_1
# file1.txt
# new_file.txt

# .suffix is used for explicitly only file extension for dir its empty
# print(my_dir.suffix)
# print(my_file.suffix)
# print(new_file.suffix)
#     
# .txt
# .txt

# .stem is used for explicitly name of file without extension
# print(my_dir.stem)
# print(my_file.stem)
# print(new_file.stem)
# Directory_1
# file1
# new_file

# all path objects need not to exists in our real dir
# to check it use .exists()
# print(my_dir.exists())
# print(my_file.exists())
# print(new_file.exists())
# True
# True
# False

# .parent also relative gives upper dir if its working its .
# print(my_dir.parent)
# print(my_dir.parent.parent)
# print(my_file.parent)
# print(new_file.parent)
# print(new_file.parent.parent)
# .
# .
# .
# Directory_1
# .

# now so far we have seen relative paths to get absolute paths
# two ways to get absolute paths
# 1 is to use aboslute method (we can use it one path leads to . or original obj)

# now see parent ie working dir right
# print(my_dir.parent.absolute())
# O:\tut\corey_03
# we r getting absolut path ie our project working dir

# or we can apply absolute on object inside our dir
# that gives path to curr + obj then we go for it parent
# print(my_dir.absolute())
# print(my_dir.absolute().parent)
# O:\tut\corey_03\Directory_1
# O:\tut\corey_03

# 2nd way is to use resolve method (mostly used)
# what it does was gives abs path but also resolves any sim links or relative dir references
# print(my_dir.resolve())
# O:\tut\corey_03\Directory_1
# as we can no chnage same as earlier absolute method

# actually um we use .. for parent dir reference
# as it doesnt work with 1st method absolute since it cant normalize ..
# p = Path("..")
# print(p)
# ..

# print(p.absolute())
# O:\tut\corey_03\..
# actually we thought .. will move up ans show O\tut\
# but its not woking as expected 

# lets try the same with 2nd way ie resolve()
# print(p.resolve())
# O:\tut

# the best practice is to go for special variale ie __file__
# which gives curr file applying resolve gives abs path
# p = Path(__file__).resolve()
# print(p)
# O:\tut\corey_03\149_pathlib.py
# and now to get um working dir use parent on it
# print(p.parent)
# O:\tut\corey_03

# p = Path("~/dotfiles").resolve()
# print(p)
# O:\tut\corey_03\~\dotfiles
# this doesnt worked as expected not reached home dir

# p = Path("~/dotfiles").expanduser()
# print(p)
# C:\Users\Vijay Karthik\dotfiles
# now this expanduser makes it possible by expanding ~ to users hoem dir
# it doesnt check does the path exists or not

# the better option is to
# p = Path.home() / "dotfiles"
# print(p)
# C:\Users\Vijay Karthik\dotfiles

# now lets try to search files in dir
dotfiles = Path.home() / "dotfiles"
# print(dotfiles)
# C:\Users\Vijay Karthik\dotfiles

# for p in dotfiles.iterdir():
#     print(p)
# this produces error since my system dont have such dir
# it only works if that dir exists

# for p in dotfiles.glob("*vscode*"):
#     print(p)
# this also same produce error since dotfiles dont exists for mine
# glob helps us search for vscode named files/dir in given path

# to also need to search nested inside dir to use recursive glob
# for p in dotfiles.rglob("*vscode*"):
#     print(p)

# and one more thing that its case sensitive search
# for case insensitive use case_sensitive =  False 
# for p in dotfiles.rglob("*vscode*", case_sensitive=False):
#     print(p)

# lets try to open a file given path
# p = Path("states.json")
# with open(p) as f:
#     print(f.read())

# there might be some cases where pathlib will be wrong choice
# like delete moving files etc
# p = Path("TempDir")
# print(p.exists())
# p.mkdir()
# print(p.exists())
# p.rmdir()
# print(p.exists())

# say if we wanted to create nested dir
p = Path("TempDir/SubDir")
# # p.mkDir()
# this will produce error
# so we need no mention parents=True
# so it creates parent along the way if they dont exists
# p.mkdir(parents=True)

# we cant delete non empty dir
# p.rm_dir()
# use shutil module to delete non empty directories
# import shutil
# shutil.rmtree("TempDir")

# lets create a file
# p = Path("tempfile.txt")
# p.touch()
# this creates file if it doesnt exists
# if it exists it updates the last updated time

# lets rename
p = Path("tempfile.txt")
# p.rename("test_file.txt")
# there is any caution using it
# ie if our new name file aleardy exists then that file will be overwrittem
# so be carefully explicitly check if it nit exists then only rename
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'tempfile.txt' -> 'test_file.txt'
# as you can see in windows we r gettogn error forrenaming as existign fike
# in mac or linux we cant gurantee that it can be overwrittem

# so use replace method which acts same in all os
# and use check if that doesnt exists
# since we cant rely 100% on method

# lest remove a file
# use unlink() to delete
# p.unlink()

# as pathlib is most reliable
# still its better to use os module and shutil module in edge cases
# getting env variables
# ans also pathlib not provided adv stuff like removing non empty dir and copying files
