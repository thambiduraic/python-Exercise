# Write a program to create a function show_employee()
# using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call
# then assign default value 9000 to salary
#
# Given:
#
# showEmployee("Ben", 12000)
# showEmployee("Jessa")
#
# Expected output:
#
# Name: Ben salary: 12000
# Name: Jessa salary: 9000

def show_employee(name, salary=9000):
    print('Name: {} salary: {}'.format(name, salary))


show_employee('ben', 12000)
show_employee('jessa')
