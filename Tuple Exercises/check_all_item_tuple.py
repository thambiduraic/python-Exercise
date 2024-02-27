# tuple1 = (45, 45, 45, 45)

# Expected output : True

tuple1 = (45, 45, 45, 45)

res = all(i == tuple1[0] for i in tuple1)

print(res)