# Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
#
# Given:
#
# str1 = "Emma25 is Data scientist50 and AI Expert"
#
# Expected Output:
#
# Emma25
# scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"
res = []
temp = str1.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
for i in res:
    print(i)
