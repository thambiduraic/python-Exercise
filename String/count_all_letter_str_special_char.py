# Count all letters, digits, and special symbols from a given string
#
# Given:
#
# str1 = "P@#yn26at^&i5ve"
#
# Expected Outcome:
#
# Total counts of chars, digits, and symbols
#
# Chars = 8
# Digits = 3
# Symbol = 4

def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print(" Chars =", char_count,"\n", "Digits =", digit_count,"\n", "Symbol =", symbol_count)


print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols("P@yn2at&#i5ve")
