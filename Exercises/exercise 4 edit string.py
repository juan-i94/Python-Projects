# Write a program to remove characters from a string starting from zero up to n and return a new string.
#
# For example:
#
# remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x


print('Removing characters from a string')
print(remove_chars('locomotion', 4))

# todo muy lindo pero no entiendo como hacer para ingresar el input por mi cuenta sin que me tire shadowed name
