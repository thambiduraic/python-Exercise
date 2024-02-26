# Reverse a given integer number

# Given:

# 76542

# Expected output:

# 24567

num = 76542
rev = 0

while num > 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print(rev)
