# Write a program to create a recursive function
# to calculate the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself again and again.
#
# Expected Output:
#
# 55

def recursive_func(num):
    if num > 0:
        return num + recursive_func(num - 1)
    else:
        return 0


print(recursive_func(10))
