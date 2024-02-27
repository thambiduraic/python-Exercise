# Write a Python program to create a new dictionary 
# by extracting the mentioned keys from the below dictionary.

# Given dictionary:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# Expected output:

# {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

res = {k: sample_dict[k] for k in keys}

print(res)