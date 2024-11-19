# Write a program to create a new string made of the middle three characters of an input string.
# Given:

# Case 1
str1 = "JhonDipPeta"
# Output Dip

l = len(str1)
mi = int(l / 2)

print(str1, 'has', l, 'characters')
print('the middle word is', str1[mi])  # trae la letra que esta en ese indice
print('the middle three caracters are', str1[mi - 1:mi + 2])

print(mi, mi - 1, mi + 2)  # trae el numero de indice
