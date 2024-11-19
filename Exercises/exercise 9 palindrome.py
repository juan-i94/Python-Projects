# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
#
# Expected Output:
# original number 121
# Yes. given number is palindrome number
# or
# original number 125
# No. given number is not palindrome number


def palindrome_check(num):
    print('Original Number:', num)
    original_num = num

    # reverse num
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    # check for palindrome
    if reversed_num == original_num:
        print('Is Palindrome')
    else:
        print('Is not Palindrome')

input_num = int(input('check number'))

palindrome_check(input_num)
