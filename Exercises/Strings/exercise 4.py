# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:
# str1 = PyNaTive
# Expected Output:
# yaivePNT

str1 = 'PyNaTive'
print('original word', str1)

uppercase = []
lowercase = []

for i in str1:
    if i.islower():
        lowercase.append(i)
    else:
        uppercase.append(i)

sortedlist = ''.join(lowercase+uppercase)

print(sortedlist)

