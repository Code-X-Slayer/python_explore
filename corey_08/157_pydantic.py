# we can do data validate instead pydantic ourselves
# imagine complex nested data having manual validation n checking would be extremely overwhelming

# manual
def create_user(username, email, age):
    if not isinstance(username, str):
        raise ValueError("username must be a str")
    if not isinstance(email, str):
        raise ValueError("email must be a str")
    if not isinstance(age, int):
        raise ValueError("age must be int")
    return {"username": username, "email": email, "age": age}

# user1 = create_user("corey","corey@gmail.com", 30)
# print(user1)
# user2 = create_user("test",None,"old")
# ValueError: email must be a str

# pydantic way (similar to dataclass)
# but dataclasses dont validate anything runtime
# also unlike manual which raise one each time pydantic shows all validation errors once
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    age: int

# user1 = User(username="corey", email="corey@gmail.com", age=30)
# print(user1)
# user2 = User(username="test", email=None, age="old")
# pydantic_core._pydantic_core.ValidationError: 2 validation errors for User
# email
#   Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
#     For further information visit https://errors.pydantic.dev/2.13/v/string_type
# age
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='old', input_type=str]

# lets see pydantic
class User(BaseModel):
    username: str
    email: str

# as of now both r needed missing values too produce error
# lets have def values
class User(BaseModel):
    username: str
    email: str
    created_at: datetime | None = None

user1 = User(username="corey", email="corey@gmail.com")
# print(user1)
# username='corey' email='corey@gmail.com' created_at=None

# access using dot operator like python object
# print(user1.username)
# print(user1.created_at)
# corey
# None

# btw its dont reevaluate on reassignment by def

# user1 = User(username="corey", email="corey@gmail.com")
# print(user1)
# user1.created_at = "other datatype"
# print(user1)
# username='corey' email='corey@gmail.com' created_at=None
# username='corey' email='corey@gmail.com' created_at='other datatype'

# if we want to convert our model to a dict use model_dump() method
user1 = User(username="corey", email="corey@gmail.com")
# print(user1.model_dump())
# {'username': 'corey', 'email': 'corey@gmail.com', 'created_at': None}

# if we want simillarly as json we can use model_dump_json() method
# print(user1.model_dump_json(indent=2))
# {
#   "username": "corey",
#   "email": "corey@gmail.com",
#   "created_at": null
# }

class User(BaseModel):
    uid: int
    username: str
    email: str
    created_at: datetime | None = None

# pydantic has automatically enabled type coersion
from pydantic import ValidationError

# try:
#     user1 = User(uid="123", username=None, email=123)
# except ValidationError as e:
#     print(e)

# we expected 3 errors but git 2 since uid str123 converted to int
# but int wasnt converted to str in case of email
# 2 validation errors for User
# username
#   Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
#     For further information visit https://errors.pydantic.dev/2.13/v/string_type
# email
#   Input should be a valid string [type=string_type, input_value=123, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.13/v/string_type

# to have empty list by def
# in normal python we cant have default = [] sicne its eval once at start not for every call
# but in pydantic we have a better altrernavtive ie Field(default_factory)
# default_factory is a simple function that gets called to create a new def value each time u create an instance
# created_at: datetime = datetime.now(UTC)
# this wot work as explained these def values created once at class and then its eval each time
# so all calls will ref to same timestamp created at start 
# so to resolve we need to use default_factory with a func that will be exec each time as we create an instance
# created_at: datetime = Field(default_factory=datetime.now(tz=UTC))
# u think this is fine but func call is static i mean no dynamic param and it will be same eval once
# so now we need somehow need not to exec our function but also set tz to UTC
# one way to do is using lambda since its an anonymous function making it run each time instance created
# might preferable way to do this using partial from functools
# since partial allows prefill some arg to function and it retursn an unexec function
# we can use pipe operator when we need multiple datatypes allowed
# say we wanna take only from a set of options to do so we need Literal

from pydantic import Field
from datetime import UTC
from functools import partial
from typing import Literal

class BlogPost(BaseModel):
    title: str
    content: str
    author_id: str | int

    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = "draft"

# this is basic usage of BaseModel for params with def values using Field
# vut Field can be do a lot more like def values , constraints too
# like min, max values or patterns or length constarints 
# to add contarints its recommended to use Annotated from typing

from typing import Annotated

class User(BaseModel):
    uid: Annotated[int, Field(gt=0)]
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: str
    age: Annotated[int, Field(ge=13, le=130)]

# try:
#     user1 = User(uid=0, username="cs", email="cs@gm.com", age=12)
# except ValidationError as e:
#     print(e)

# 3 validation errors for User
# uid
#   Input should be greater than 0 [type=greater_than, input_value=0, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.13/v/greater_than
# username
#   String should have at least 3 characters [type=string_too_short, input_value='cs', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
# age
#   Input should be greater than or equal to 13 [type=greater_than_equal, input_value=12, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.13/v/greater_than_equal

class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=20)]
    content: Annotated[str, Field(min_length=1)]
    author_id: str | int

    view_count: Annotated[int, Field(ge=0)] = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = "draft"

    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

# as of now we r defining all constraints manually
# there r some built in constarints fro soem types in pydantic
# they save a some time isntead adding all constraints ourself use existing ones
# like PositiveInt, httpUrl, EmailStr etc refer docs
# and some of them needed use of extrenal lib like EmailStr needs email validator library
# when u install pydantic u only install core but not all theses addn helping ext libraries

from uuid import UUID, uuid4
from pydantic import EmailStr, HttpUrl, SecretStr

class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20)]
    password: SecretStr
    website: HttpUrl | None = None
    email: EmailStr | None = None

user = User(username="corey", password="NOTSHOWN", website="https://coreyms.com/")
# i juts intended for better view it prints normally
# print(user)
# uid = UUID('ef71cba7-39cf-46ec-a055-20a3af4ca7f0')
# username='corey'
# password=SecretStr('**********')
# website=HttpUrl('https://coreyms.com/')

# as we r not gonna satisy with given builtin validators 
# we need our custom validators since we have custom logic
from pydantic import field_validator, model_validator, ValidationInfo

class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr
    password: SecretStr
    website: HttpUrl | None = None
    age: Annotated[int, Field(ge=13, le=130)]
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True
    full_name: str | None = None

    # custom validation for username if all base above fine then this will be checked
    # we r validating(checking alnum) and normalizing(lowercase)
    @field_validator("username")
    @classmethod
    def validate_username(cls, v:str) -> str:
        if not v.replace('_','').isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()
    
    # as above one doen after tpe chacking n basic data validations
    # in somecases we wnat to preprocess abit then do basic validations
    # this can be altered by using mode
    @field_validator("website", mode='before')
    @classmethod
    def validate_website(cls, v:str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v
    
# as field validators used to validate a single atribute
# model validator will be used to validate whole model or mult attributes
class UserRegistration(BaseModel):
    email:EmailStr
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def password_mismatch(self) -> UserRegistration:
        if self.password != self.confirm_password:
            raise ValueError("Passwords dont match")
        return self
    
# lets see computed fields
from pydantic import computed_field

class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20)]
    age: Annotated[int, Field(ge=13, le=130)]
    email: EmailStr
    password: SecretStr
    bio: str = ""
    website: HttpUrl | None = None
    verified_at: datetime | None = None
    is_active: bool = True
    full_name: str | None = None
    follower_count: int = 0
    first_name: str | None = None
    last_name: str | None = None
    @field_validator("username")
    @classmethod
    def validate_username(cls, v:str) -> str:
        if not v.replace('_','').isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()
    @field_validator("website", mode='before')
    @classmethod
    def validate_website(cls, v:str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v
    
    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000
    
user = User(username="coreyschafer", email="xyz@gmail.com", age=30, password="hidden")
# print(user.model_dump_json(indent=2))
# {
#   "uid": "643a718a-87b3-4923-a8ce-9fc837772a59",
#   "username": "coreyschafer",
#   "age": 30,
#   "email": "xyz@gmail.com",
#   "password": "**********",
#   "bio": "",
#   "website": null,
#   "verified_at": null,
#   "is_active": true,
#   "full_name": null,
#   "follower_count": 0,
#   "first_name": null,
#   "last_name": null,
#   "display_name": "coreyschafer",
#   "is_influencer": false
# }
user = User(username="coreyschafer", email="xyz@gmail.com", age=30, password="hidden", first_name="Corey", last_name="Schafer")
# print(user.model_dump_json(indent=2))
# {
#   "uid": "d3ed9223-b550-40f5-b8cf-8c215b9d6a11",
#   "username": "coreyschafer",
#   "age": 30,
#   "email": "xyz@gmail.com",
#   "password": "**********",
#   "bio": "",
#   "website": null,
#   "verified_at": null,
#   "is_active": true,
#   "full_name": null,
#   "follower_count": 0,
#   "first_name": "Corey",
#   "last_name": "Schafer",
#   "display_name": "Corey Schafer",
#   "is_influencer": false
# }
user = User(username="coreyschafer", email="xyz@gmail.com", age=30, password="hidden", first_name="Corey", last_name="Schafer", follower_count=10000)
# print(user.model_dump_json(indent=2))
# {
#   "uid": "f089abc5-9804-427a-8002-ac7d7d846523",
#   "username": "coreyschafer",
#   "age": 30,
#   "email": "xyz@gmail.com",
#   "password": "**********",
#   "bio": "",
#   "website": null,
#   "verified_at": null,
#   "is_active": true,
#   "full_name": null,
#   "follower_count": 10000,
#   "first_name": "Corey",
#   "last_name": "Schafer",
#   "display_name": "Corey Schafer",
#   "is_influencer": true
# }

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=20)]
    content: Annotated[str, Field(min_length=1)]
    author: User
    view_count: Annotated[int, Field(ge=0)] = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = "draft"
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

    comments: list[Comment] = Field(default_factory=list)

# in this way we can nest models pydantic gonna check each model nested too
# to create one we can
# post = BlogPost(**post_data) # unpcaking dict
# post = BlogPost.model_validate(post_data) # another way

# as far now we have seen model_dump and model_dump_json options only
# but there are lot more options for controlling how ur data is serialozed
# one common use case is working with api where representation uses diff field_names tha internal python names
# say for ex js frontedn uses cameCase but we used snake_case 
# and there may be some internal fields that we dont wanna expose
# we r gonna import ConfigDict from pydantic

# lets see adv topics
# aliases
# they offer us another name kind of for each attrib
# so if the inout param keyword was giuven by alias we can access it
# and while outputiing too we can make print alias instead attrib

from pydantic import ConfigDict

class Demo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    attrib: int = Field(alias="alias", default_factory=0)

d = Demo(alias=1)
print(d.model_dump_json(indent=2))
print(d.model_dump_json(indent=2, by_alias=True))
# {
#   "attrib": 1
# }
# {
#   "alias": 1
# }

# Serialization (Deciding what to include or exclude)
# say we wanna exclude a few printing all
# print(model.model_dump_json(exclude={params to exclude}))
# say we wanna include a few and exclude most
# print(model.model_dump_json(include={params to include}))

# till now we have manually created models or usin python dict
# lest see how to do it from direct json (just liek api gives us)
import json

# as we seen another way like
# model_obj = Model.model_validate(data or python dict)
# we can use model_validate_json
# model_obj = Model.model_validate_json(json_str)

# so so far adv concpets we saw
# we can use alias to hanlde name mismatches n frontend diff case ones
# and also to serialoze decide what to incldue or exclude
# and to dig deep the model_config plays a crucia; rol in how pydantic model works

# u remeber the fact was pydantuc tries type coresion liek int to str by def
# we can alter its behaiour n make it strciter
# its as simple as
# model_config = ConfigDict(strict=True)

# and also one thing was allows extra params taht r not mentioned in model
# model_config = ConfigDict(extra="allow")
# we can also make it raise error
# model_config = ConfigDict(extra="forbid")
# we can make it raise error
# to validate re assignment
# model_config = ConfigDict(validate_assignment=True)

# sometimes we wanna make immutable models aka frozen model
# where data cant be chnaged at all after creation
# model_config = ConfigDict(frozen=True)

# this is the reason all why pydantic is useful for data validation and flexibity it gave
# since it does all of this with pretty less boiler plate code
# as type hints not just stop as use for data validation but also ide completes and inline docs
# FastAPI web framework underhood uses pydantic for request n response validation
# sqlmodels too use pydantic u will see its most used everywhere in oython eco system 