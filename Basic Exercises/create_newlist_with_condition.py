# Create a new list from two list using the following condition

# Given two list of numbers, 
# write a program to create a new list 
# such that the new list should contain odd numbers from the first list 
# and even numbers from the second list.

# Expected Output:

# result list: [25, 35, 40, 60, 90]

def list_join(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            result_list.append(num)
    
    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(list_join(list1, list2))