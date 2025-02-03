# This is a calculator project.
# i need it to sum, rest, multiply, and divide.


def sum(num1, num2):
    sum_result = num1 + num2
    return sum_result

num1 = float(input())

operator = input()

num2 = float(input())

print(sum(num1, num2))