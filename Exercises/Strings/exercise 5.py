# Count all letters, digits, and special symbols from a given string
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for i in str1:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1


print('Total counts of characters, digits and symbols:'
      '\nChars:', chars,
      '\nDigits:', digits,
      '\nSymbols:', symbols)

