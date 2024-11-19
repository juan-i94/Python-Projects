# Iterate the given list of numbers and print only those numbers which are divisible by 5
#
# Expected Output:
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

givenlist = [10, 20, 33, 46, 55]

for n in givenlist:
    if n % 5 == 0:
        print(n)

# Modulus %
# The remainder of the division of left operand by the right.
# The modulus operator is denoted by a % symbol.
# In simple terms, the Modulus operator divides one value by a second and gives the remainder as a result.

