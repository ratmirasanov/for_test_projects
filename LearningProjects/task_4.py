"""Task 4."""


def sum_elements(argument1):
    """Calculate sum of elements in the list."""

    if isinstance(argument1, list):
        sum_of_elements = 0
        for element in argument1:
            sum_of_elements += element

    return sum_of_elements


def multiply_elements(argument1):
    """Calculate multiplication of elements in the list."""

    if isinstance(argument1, list):
        multiplication_of_elements = 1
        for element in argument1:
            multiplication_of_elements *= element

    return multiplication_of_elements


print("Sum of elements in the list {} is {}".format([3, 4, 4, 1], sum_elements([3, 4, 4, 1])))
print("Multiplication of elements in the list {} is {}".format([3, 4, 4, 1],
                                                               multiply_elements([3, 4, 4, 1])))
