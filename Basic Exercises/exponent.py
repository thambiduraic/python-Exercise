# Expected output

# Case 1:                               # Case 2:

# base = 2                              # base = 5
# exponent = 5                          # exponent = 4

# 2 raises to the power of 5: 32        # 5 raises to the power of 4 is: 625  
# i.e. (2 *2 * 2 *2 *2 = 32)            # i.e. (5 *5 * 5 *5 = 625)

def exponent(base, expo):
    result = base ** expo
    print("{} raises to the power of {}: {}".format(base, expo, result))

exponent(2, 5)
exponent(5, 4)