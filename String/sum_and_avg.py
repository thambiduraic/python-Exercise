# Calculate the sum and average of the digits present in a string
# Given a string s1,
# write a program to return the sum and average of the digits
# that appear in the string, ignoring all other characters.

# Given:

# str1 = "PYnative29@#8496"

# Excepted:

# Sum is: 38 Average is  6.333333333333333

str1 = "PYnative29@#8496"

list1 = []
total = 0
for x in str1:
    if x.isdigit():
        list1.append(x)

for i in list1:
    total += int(i)

print("Total : {} Average {}:".format(total, total/len(list1)))
