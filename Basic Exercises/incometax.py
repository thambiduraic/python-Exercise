# Taxable           Income	    Rate (in %)

# First             $10,000	    0
# Next              $10,000	    10
# The remaining                 20

# Expected Output:

# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

income = 45000
tax = 0

if(income <= 10000):
    tax = 0

elif(income <= 20000):
    amount = income - 10000
    tax = amount * 10 / 100

else:
    # first 10000 0% tax
    tax = 0
    
    # next 10000 10% tax
    tax = 10000 * 10 / 100
    
    # the remaining income 20% tax
    tax += (income - 20000) * 20 / 100

print(tax)