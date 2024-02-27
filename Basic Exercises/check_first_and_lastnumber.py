# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

def check(lists):
    # list comparision
    if(lists[0] == lists[-1]):
        return "True"
    else:
        return "False"

list1 = [10,20,30,40,10]
list2 = [20,40,80]

result1 = check(list1)
print(result1)

result2 = check(list2)
print(result2)