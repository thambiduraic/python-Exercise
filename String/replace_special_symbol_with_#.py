# Replace each special symbol with # in the following string
# Given:
#
# str1 = '/*Jon is @developer & musician!!'
# Expected Output:
#
# ##Jon is #developer # musician##

import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)