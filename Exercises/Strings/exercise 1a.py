# https://pynative.com/python-string-exercise/
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Given:
# str1 = "James"
# Expected Output:
#
# Jms

str1: str = 'James'
l = len(str1)
mi = int(l / 2)

first_letter = str1[0]
last_letter = str1[l - 1]
middle_letter = str1[mi]


print('Original string is', str1)
print('New string is', first_letter + middle_letter + last_letter)

