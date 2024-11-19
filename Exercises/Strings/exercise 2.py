# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
#
# Given:
#
# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:
#
# AuKellylt

s1 = 'Ault'
s2: str = 'Kelly'

l1 = len(s1)
mi1 = int(l1 / 2)

a = s1[:mi1]  # [:mil1] se lee desde el principio hasta middle index
b = s1[mi1:]  # [mil1:] se lee desde el middle index hasta el final
print(a,b)
print(a + s2 + b)


