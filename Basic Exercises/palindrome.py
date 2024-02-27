# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. 
# For example, 545, is the palindrome numbers

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number


def palindrome(num):

    original_num = num
    reverse_num = 0

    # reverse logic
    while num > 0:
        reminder = num % 10
        reverse_num = (reverse_num * 10) + reminder
        num = num // 10
    
    # check numbers
    if(original_num == reverse_num):
        print("Number ", original_num ," is a palindrome number")
    else:
        print("Number ", original_num ," is not a palindrome number")

palindrome(121)
palindrome(245)