# Write a program to print the following start pattern using the for loop

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

row = 5

for i in range(1, row+1):
    for j in range(i):
        print('*',end=' ')
    print('\r')

for x in range(row, 0, -1):
    for y in range(x-1):
        print('*', end=' ')
    print('\r')