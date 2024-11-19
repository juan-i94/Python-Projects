# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
#
# Given:
#
# s1 = "America"
# s2 = "Japan"
# Expected Output:
#
# AJrpan

s1 = "America"
s2 = "Japan"

# my code
################

# s1 = "America"
# s2 = "Japan"
#
len1 = len(s1)
mi1 = int(len1 / 2)
# first1 = s1[0]
# middle1 = s1[mi1]
last1 = s1[len1 - 1]
#
len2 = len(s2)
mi2 = int(len2 / 2)
# first2 = s2[0]
# middle2 = s2[mi2]
last2 = s2[len2 - 1]
#
# print(first1 + first2 + middle1 + middle2 + last1 + last2)

# and now answer code, lo hacen con una funcion
############################################################

def mix_strings(s1, s2):

     first_char = s1[0] + s2[0]

     middle_char = s1[mi1] + s2[mi2]

     last_char = last1 + last2

     res = first_char + middle_char + last_char

     print(res)


mix_strings(s1, s2)

