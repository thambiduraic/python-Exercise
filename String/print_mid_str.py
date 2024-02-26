# Create a string made of the middle three characters
# Write a program to create a new string
# made of the middle three characters of an input string

# Case 1

# str1 = "JhonDipPeta"

# Output

# Dip

# Case 2

# str2 = "JaSonAy"

# Output

# Son

str1 = "jasonAy"

mid = int(len(str1) / 2)

res = str1[mid-1 : mid+2]

print(res)