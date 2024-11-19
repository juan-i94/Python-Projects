# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
# pynative
# 01234567

word = input('Enter a string value: ')
size = len(word)

print('Original word is', word)
print('Printing only even index chars:')

for i in range(0, size - 1, 2):
    print(i, word[i])

# I don't understand the structure of the "for i in range" is i the name of the loop?
# i is a variable that stores each number of the iteration?
