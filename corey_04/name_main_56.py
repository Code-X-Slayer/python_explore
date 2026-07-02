# when python runs a program it always created special variables
# and assigns them initial values and name is one of those

# print(f"__name__ is {__name__}")
# this lines op when runned itsle slf was __main__
# but other code imported it it becomes the script name
# __name__ is __main__
# __name__ is name_main_56

# so simply to say
# when imported it will run
# to segregate section that runs when its run independent and from imported
# we use __name__ == '__main__' so that it only executes when its run independently
# isolating from import running

# if __name__ == '__main__':
#     print("run directly")
# else:
#     print("run via import")

# > python .\name_main_56.py
# run directly
# > python .\sample.py      
# run via import

print("this will run always")
def main():
    print("this will run only when run independently")
if __name__ == '__main__':
    main()

# PS > python .\name_main_56.py
# this will run always
# this will run only when run independently
# PS > python .\sample.py      
# this will run always