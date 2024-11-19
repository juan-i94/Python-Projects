#https://pynative.com/python-basic-exercise-for-beginners/
# Given two integer numbers, return their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

# para crear una user defined function usamos la palabra def
# def function_name(parameter1, parameter2):
# function body
# write some action
# #return value

num1 = int(input('First number: '))
num2 = int(input('Second number: '))


def multiplication_or_sum(num1, num2):
    product = num1 * num2  # la funcion primero calcula el producto
    if product <= 1000:  # si "producto" es menor o igual a mil
        return product  # devuelve el producto
    else:
        return num1 + num2  # caso contrario devuelve la suma de los dos numeros


result = multiplication_or_sum(num1, num2)
print('The result is: ', result)
