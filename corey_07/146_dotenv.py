# we dont have to hardcode api, pass, senesitive data
# 1st advantage is cross platform(window mac) dont care how each handles
# 2nd env varset at project level not systsem level so multi proj dont collide

# pip install python-dotenv
# create .env file (make sure its .gitignore so u dont push it)

import os
from dotenv import load_dotenv

# print(os.environ)
# to check sys env variables

# now to access we have load from env file to do that
load_dotenv()

# now to access loaded env file values
API_KEY = os.getenv("API_KEY")
print(API_KEY)
# ABCD1234

# about env file syntax
# no spaces allowed around sign assignment
# you can add comments using #
# make sure all loaded values will be string
# if they r supposed to number u have to cast

NUM = os.getenv("NUM")
print(type(NUM))
# <class 'str'>

USERNAME = os.getenv("USERNAME")
print(USERNAME)
# Vijay Karthik
# expected Code X Slayer but sys env not overrided

# env file dont ovveride system env variables with same value
# 1st solution is simply change variable name
# 2nd solution u can override load_dotenv(override=True)
# 2nd one is not recommended so simply change var name

# USER_NAME = os.getenv("USER_NAME")
# print(USER_NAME)
# Code X Slayer

# print(os.getenv("USER")) None if not exists

# wehn u use singe quotes cant use spec char
ADDRESS = os.getenv('ADDRESS')
print(ADDRESS)
# 123\nAdd

# to get new lines like spec char use double quotes
DEMO = os.getenv('DEMO')
print(DEMO)
# 123
# Add

# to use existing variables to expand new ones
EMAIL = os.getenv("EMAIL")
print(EMAIL)
# Code X Slayer@gmail.com