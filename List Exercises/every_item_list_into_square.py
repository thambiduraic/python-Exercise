# Given a list of numbers. 
# write a program to turn every item of a list into its square.

# Given:  numbers = [1, 2, 3, 4, 5, 6, 7]

# Expected output:    [1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]

# result = []
# for i in numbers:
#     result.append(i*i)
# print(result)

result = [i * i for i in numbers]
print(result)