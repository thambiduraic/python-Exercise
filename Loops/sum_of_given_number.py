# Calculate the sum of all numbers from 1 to a given number
#
# Expected Output:
#
# Enter number 10
# Sum is:  55

number = int(input("Enter a number: "))
sum_of_numbers = 0
for i in range(1, number+1):
    sum_of_numbers += i

print(sum_of_numbers)
