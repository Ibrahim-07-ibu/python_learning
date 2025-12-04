# # this work is called as deserialisiastion

# import json

# # data = '{"name": "Alice", "age": 30, "isStudent": false, "courses": ["Math", "Science", "History"], "address": {"street": "123 Main St", "city": "Anytown", "zip": 12345}}'

# # x = json.loads(data)

# # print(x)
# # print(x['address']['city'])

# # print('skills'[1])

# dictionary ={"name": "Alice", "age": 30, "isStudent": False, "courses": ["Math", "Science", "History"], "address": {"street": "123 Main St", "city": "Anytown", "zip": 12345}}

# y = json.dumps(dictionary)
# print(y)

# print(type(y))


import json
import requests
# Step 1: Make a GET request to the API
response = requests.get("https://randomuser.me/api/")
# Step 2: Convert response JSON → Python dict
data = response.json()
# Step 3: Extract some values
user = data["results"][0]
name = user["name"]["first"]
email = user["email"]
city = user["location"]["city"]
print("Name:", name)
print("Email:", email)
print("City:", city)

# with open("data.json","r") as f :
#     data = json.load(f)
# print(data)