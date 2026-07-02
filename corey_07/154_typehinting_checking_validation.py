# python is not statistically type language
# so we dont need to specify data type
# and data type of one var can change over script
# it gives us flexibity but also lead to bugs harder to debug

# type hints tells what we expect somthing to be
# type checking is static analysis to make sure we r sticking to declared types before code runs
# data validation happens at runtime to make sure data meet req

# type hinting also called annotations
# adding type info to var func params or return values
# improves code readability and maintanability
# kind of looks self documenting and easy to work with
# it also helps with ide autocomplete
# u can type hinting everything but it can be excessive
# juts sticking with function params n return type id best use case

def create_user(first: str, last: str, age: int) -> dict:
    email = f"{first.lower()}_{last.lower()}@example.com"
    return {
        "first" : first,
        "last" : last,
        "email" : email,
        "age" : age
    }

# user1 = create_user("corey", "schafer", 30)
# print(user1)
# {'first': 'corey', 'last': 'schafer', 'email': 'corey_schafer@example.com', 'age': 30}

# btw type hints were just meta dat it doesnt throw any error
# if wrong datatype passed

# user2 = create_user("corey", "schafer", "thirty")
# print(user2)
# {'first': 'corey', 'last': 'schafer', 'email': 'corey_schafer@example.com', 'age': 'thirty'}

# so they dont enforce anything its just giving hints

# static type checking
# it analyzes code before running (static code)
# to make sure types u mentioned are correct
# so it happens before runtime and catches mismatches earlier

# btw its not built in python
# we have to use external tools like mypy

# now if u intsall n enable extension
# it shows the erros where u mismatched type

# its showing 
# Argument 3 to "create_user" has incompatible type "str"; expected "int"
# so type hints just meta data to see like hits n dont mention if we mismatch
# whereas type checking like mypy does static check m show error
# but it doesnt stop it from execution
# btw type checking also cant guard from dyanmic data
# say api key from env or user input or datafrom files
# since its static check it cant tell what type it is


# data validation
# this is dynamic ie checks runtime
# make sure that data meets spec req

# it goes beyong typechecking when expec data type mismatches
# wither it can be diff type or else outside mentioned range formats etc
# it guards againts all such bad vlaues rasing validation errors

# imp note : data validation needs type hints
# doing data validation manually is so much boiler plate code
def create_user_v1(first: str, last: str, age: int) -> dict:
    email = f"{first.lower()}_{last.lower()}@example.com"
    if not isinstance(first, str):
        raise TypeError("first must be str")
    if not isinstance(last, str):
        raise TypeError("last must be str")
    if not isinstance(age, int):
        raise TypeError("age must be int")
    return {
        "first" : first,
        "last" : last,
        "email" : email,
        "age" : age
    }

# user3 = create_user_v1(1,2,3)
# AttributeError: 'int' object has no attribute 'lower'
# user3 = create_user_v1('first',2,3)
# AttributeError: 'int' object has no attribute 'lower'
# user3 = create_user_v1('first','last','thirty')
# TypeError: age must be int

# uts so hard to update n redundant to write such boiler plate
# we can do data validation using pydantic

from pydantic import validate_call

@validate_call
def create_user_v2(first: str, last: str, age: int) -> dict:
    email = f"{first.lower()}_{last.lower()}@example.com"
    return {
        "first" : first,
        "last" : last,
        "email" : email,
        "age" : age
    }

# user3 = create_user_v2(1,2,'thirty')
# pydantic_core._pydantic_core.ValidationError: 3 validation errors for create_user_v2
# 0
#   Input should be a valid string [type=string_type, input_value=1, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type
# 1
#   Input should be a valid string [type=string_type, input_value=2, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type
# 2
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='thirty', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/int_parsing

user4 = create_user_v2('corey', 'schafer', '30')
print(user4)
# {'first': 'corey', 'last': 'schafer', 'email': 'corey_schafer@example.com', 'age': 30}
# as you can pydantic auto casted str to int
# its giving type check error but data validation handles

# by def its try to caste like above
# if you want it to be strict u can do it

# data validation not much useful in static values
# its used with dynamic data u have to protect from bad dynamic data

# type hints are just builtin with python n juts hints aka meta data
# they alone dont enforce anything but used by tools like pydantic mypy ect
