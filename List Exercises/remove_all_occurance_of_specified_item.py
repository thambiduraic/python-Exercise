# Given a Python list, write a program to remove all occurrences of item 20.

# Given : list1 = [5, 20, 15, 20, 25, 50, 20]

# Expected output : [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]

occur = 20

res = [i for i in list1 if i != occur]

print(res)