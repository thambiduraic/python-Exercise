# Create an outer function that will accept two parameters, a and b
#
# Create an inner function inside an outer function
# that will calculate the addition of a and b
#
# At last, an outer function will add 5 into addition and return it

def outer_func(num1, num2):
    def inner_func(a, b):
        return a + b
    add = inner_func(num1, num2)
    return add


print(outer_func(15, 15))
