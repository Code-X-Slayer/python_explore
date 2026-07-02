# here say age can be None so we cant mention it like
# def create_user(first: str, last: str, age: int = None) -> dict:

# to resolve for earlier version we have Optional
# from typing import Optional
# def create_user(first: str, last: str, age: Optional[int] = None) -> dict:

# latest version use pipe | to union of poss types
# def create_user(first: str, last: str, age: int | None = None) -> dict:

# btw as of now we simple mentioning dict but we can specify key value of dict
# but this is invalid as for age value can be None or int but not str
# def create_user(first: str, last: str, age: int | None = None) -> dict[str, str]:
# to resolve this we can use pipe | operator like eralier
# def create_user(first: str, last: str, age: int | None = None) -> dict[str, str | int | None]:

# now imagine a complex dict this gets lot of clumsy we can use type alias
# ie we rsimply creating a new name for existing types
# we kind of store that kind of dict with str int None values some x and we can call it

# User = dict[str, str | int | None]
# print(type(User)) <class 'types.GenericAlias'>
# we can explicitly put type beefore var name
# type User = dict[str, str | int | None]
# def create_user(first: str, last: str, age: int | None = None) -> User:

# say RGB 3 int tuple
# type RGB = tuple[int, int, int]
# type User = dict[str, str | int | RGB | None]
# def create_user(first: str, last: str, age: int | None = None, fav_color: RGB | None = None) -> User:

# lets say HSL same 3 int tuple
# type HSL = tuple[int, int, int]
# type User = dict[str, str | int | RGB | HSL | None]
# def create_user(first: str, last: str, age: int | None = None, fav_color: RGB | HSL | None = None) -> User:

# now lets say user passes (2,3,4) 
# but it doesnt know and consider hsl as rgb too
# to solve this we need to create new type (we r not creating aliases but NewType)

from typing import NewType
RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])
# type User = dict[str, str | int | RGB | HSL | None]
# now to pass we pass it like below
# (fav_color=RBG((1,2,3)))
# (fav_color=HSL((4,5,6)))
# def create_user(first: str, last: str, age: int | None = None, fav_color : RGB | None = None) -> User:

# as of now dict values can be anything iverall but cant specific
# say for age we expect int but giving str doesnt stopped
# so instead of type alias (ie we r passing all poss values)
# we need to use a typed dict for each individual key we will use TypedDict

# from typing import TypedDict

# class User(TypedDict):
#     first: str
#     last: str
#     email: str
#     age: int | None
#     fav_color : RGB | HSL | None

# now this will enforce value of each key follows corresponding types
# def create_user(first: str, last: str, age: int | None = None, fav_color : RGB | None = None) -> User:
    # email = f"{first.lower()}_{last.lower()}@example.com"
    # return {
    #     "first" : first,
    #     "last" : last,
    #     "email" : email,
    #     "age" : age,
    #     "fav_color" : fav_color
    # }


# its better to use data class
# these can have def values
# and also provide common methods for us
from dataclasses import dataclass

@dataclass
class User:
    first: str
    last: str
    email: str
    age: int | None = None
    fav_color : RGB | HSL | None = None

def create_user(first: str, last: str, age: int | None = None, fav_color : RGB | None = None) -> User:
    email = f"{first.lower()}_{last.lower()}@example.com"
    return User(
        first=first,
        last=last,
        email=email,
        age=age,
        fav_color=fav_color
    )

# lets see a beautiful example
import random

# def random_choice(items: list[User]) -> User:
#     return random.choice(items)

user1 = create_user('corey', 'schafer', age=30, fav_color=RGB((1,2,3)))
user2 = create_user('corey2', 'schafer2', age=30, fav_color=RGB((4,5,6)))

users = [user1, user2]
# say we need random user
# random_user = random_choice(users)
# print(random_user)
# User(first='corey', last='schafer', email='corey_schafer@example.com', age=30, fav_color=(1, 2, 3))

# say we need random email
# emails = [user.email for user in users]
# random_email = random_choice(emails)
# Argument 1 to "random_choice" has incompatible type "list[str]"; expected "list[User]"
# but still runs and ide autocompletes
# print(random_email)
# corey2_schafer2@example.com

# as you can see its kind of working for every type
# buts its kind of misleading as now ide expects random_email to be a User
# and it heps auto completeing with like email.first like that whihc is misleading
# we kind of want a place holder to write generic function that helps us to get random one acc

# one way to do is use any whihc kind iof good
# but loss is functionality op var ide dont know what is it
# from typing import Any
# def random_choice(values: list[Any]) -> Any:
#     return random.choice(values)

# random_user = random_choice(users)
# random_user. produces no ide auto complete

# better way to do this using TypeVar
# from typing import TypeVar

# T = TypeVar("T")
# def random_choice(values: list[T]) -> T:
#     return random.choice(values)

# random_user = random_choice(users)
# random_user. this guves auto complete

# best way to do this not pollutin name sapce
# this will boudn to that function itself
def random_choice[T](values: list[T]) -> T:
    return random.choice(values)

random_user = random_choice(users)
# random_user.t his guves auto complete

# now another banger
# say we have 3rd party package
# checker dont knwo about its output types
# so then we need to install types-package or types-*

import requests

response = requests.get('https://imgs.xkcd.com/comics/python.png')
status_code = response.status_code

status_code = "OK"
# Hint: "python3 -m pip install types-requests"
# (or run "mypy --install-types" to install all missing stub packages)
# See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
# as explained mypy cant tell what type it is needed type

# now after python -m pip install types-requests