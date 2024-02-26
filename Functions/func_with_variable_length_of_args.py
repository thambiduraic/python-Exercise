# Write a program to create function func1() to accept a variable length of arguments
# and print their value.
#
# Function call:
#
# # call function with 3 arguments
# func1(20, 40, 60)
#
# # call function with 2 arguments
# func1(80, 100)
#
# Expected Output:
#
# Printing values
# 20
# 40
# 60

def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
