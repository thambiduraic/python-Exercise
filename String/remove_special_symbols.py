# Remove special symbols / punctuation from a string
# Given:
#
# str1 = "/*Jon is @developer & musician"
# Expected Output:
#
# "Jon is developer musician"
import string

str1 = "/*Jon is @developer & musician"

res = str1.translate(str.maketrans('', '', string.punctuation))

print(res)
