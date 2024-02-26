# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2,
# write a program to return a new string
# made of s1 and s2’s first, middle, and last characters.

# Given:

# s1 = "America"
# s2 = "Japan"

# Expected Output:

# AJrpan

s1 = "America"
s2 = "japan"

first = s1[0] + s2[0]

mid_s1 = int(len(s1) / 2)  # 7 / 2 = 3
mid_s2 = int(len(s2) / 2)  # 5 / 2 = 2

mid = s1[mid_s1: mid_s1 + 1] + s2[mid_s2: mid_s2 + 1]

last = s1[-1] + s2[-1]

res = first + mid + last

print(res)
