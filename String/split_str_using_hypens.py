# Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
#
# Given:
#
# str1 = Emma-is-a-data-scientist
# Expected Output:
#
# Displaying each substring
#
# Emma
# is
# a
# data
# scientist

str1 = "Emma-is-a-data-scientist"

str2 = str1.split("-")

for i in range(len(str2)):
    print(str2[i])
