import json

# people_string = """
# {
#     "people": [
#         {
#             "name" : "John Smith",
#             "phone" : "9999999999",
#             "emails" : ["x@gmail.com", "y@office.in"],
#             "has_license" : false
#         },
#         {
#             "name" : "Jane Doe",
#             "phone" : "9999988888",
#             "emails" : null,
#             "has_license" :true
#         }
#     ]
# }
# """

# data = json.loads(people_string)
# print(data)
# print(type(data))
# <class 'dict'>
# print(type(data['people']))
# <class 'list'>

# Json maps like following in python stuff
# object -> dict
# array -> list
# string -> str
# number (int) -> int
# number (real) -> float
# true -> True
# false -> False
# null -> None

# lest try to print selected data
# for person in data['people']:
    # print(person['name'])

# lets drop phone since its personal and dump to json string
# for person in data['people']:
#     del person['phone']

# new_string = json.dumps(data)
# print(new_string)

# for better readability use intend in dumps
# new_string = json.dumps(data, indent=4)
# print(new_string)

# while dumping we can have another good practice ie sort_keys
# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)

# till now we handled data as str using json.loads and json.dumps
# lets see hwo to handle files

# with open('states.json', 'r') as f:
#     data = json.load(f)

# for state in data['states']:
#     # print(state)
#     print(state['name'], state['abbreviation'])

# for state in data['states']:
#     del state['area_codes']

# with open('states_copy.json', 'w') as f:
#     json.dump(data, f)
# this just dropped all at single line use indent

# with open('states_copy.json', 'w') as f:
#     json.dump(data, f, indent=2)

import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
# response.raise_for_status()
# # print(response)

# data = json.loads(response.text)
# # print(data)
# # [
# #     {
# #         'userId': 1, 'id': 1,
# #         'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
# #         'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
# #     },
# #     ...
# # ]

# summary = {}
# for post in data:
#     # print(post)
#     user_id = post['userId']
#     summary[user_id] = summary.get(user_id, 0) + 1

# print(summary)

url = "https://api.github.com/repos/python/cpython"

response = requests.get(url)
response.raise_for_status()

# print(response.text)

# data = json.loads(response.text)
data = response.json()
# print(data)

print(data['id'])
print(data['node_id'])
print(data['name'])
print(data['full_name'])
print(data['owner'])