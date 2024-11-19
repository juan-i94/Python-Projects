# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# Expected Output:

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False

# these are lists:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def first_last_equal(numberlist):
    print('Given list:', numberlist)

    first_number = numberlist[0]
    last_number = numberlist[-1]
    # negative index, se puede llamar el ultimo elemento de la lista con -1, anteultimo -2 y asi

    if first_number == last_number:
        return True
    else:
        return False


print('result is', first_last_equal(numbers_y))
