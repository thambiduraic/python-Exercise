#Given two integer numbers, return their product only
#if the product is equal to or lower than 1000.
#Otherwise, return their sum.

def mul_or_sum(num1, num2):
    
    product = num1 * num2

    # check product value is less then 1000
    if(product <= 1000):
        return product
    
    # else calculate the sum
    else:
        sum = num1 + num2
        return sum

result1 = mul_or_sum(20, 30)
print(result1)

result2 = mul_or_sum(40, 30)
print(result2)