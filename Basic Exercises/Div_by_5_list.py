# Iterate the given list of numbers 
# and print only those numbers which are divisible by 5.

ls = [10, 20, 33, 46, 55]
print("Given a list is ", ls)

for x in ls:
    if(x%5 == 0):
        print(x)