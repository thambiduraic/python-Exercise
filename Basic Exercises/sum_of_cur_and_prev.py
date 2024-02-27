# Write a program to iterate the first 10 numbers, 
# and in each iteration, print the sum of the current and previous number.

previous_num = 0

txt = 'printing current and previous number sum in a range({})'

print(txt.format(10))

for i in range(10):
    print('current number ', i, 'previous number', previous_num, 'sum : ', i+previous_num)
    previous_num = i