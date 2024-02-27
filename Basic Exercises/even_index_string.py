# Write a program to accept a string from the user 
# and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

string = "pynative"

print('Original string is', string)

print('printing only even index char')

len = len(string)

for i in range(len):
    if(i%2 == 0):
        print(string[i])