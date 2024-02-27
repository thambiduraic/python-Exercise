# Given : tuple1 = (10, 20, 30, 40, 50)

# Expected output : (50, 40, 30, 20, 10)

tuple1 = (10, 20, 30, 40, 50)

# list1 = list(tuple1)

# list1.reverse()

# tuple1 = tuple(list1)

tuple1 = tuple1[::-1]

print(tuple1)