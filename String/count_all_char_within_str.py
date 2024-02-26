# Write a program to count occurrences of all characters within a string
# Given:
#
# str1 = "Apple"
#
# Expected Outcome:
#
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"

dict1 = dict()

for i in str1:
    count = str1.count(i)
    dict1[i] = count

print(dict1)
