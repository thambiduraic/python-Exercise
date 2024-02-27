# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output :  ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = list(filter(None, list1))

print(result)