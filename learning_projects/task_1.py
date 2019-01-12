"""Task 1."""


def max_func(argument1, argument2):
    """Calculate max value of two numbers and return it."""

    if float(repr(argument1)) and float(repr(argument2)):

        if argument1 > argument2:

            max_value = argument1

        else:

            max_value = argument2

        return max_value

    else:

        return False


# print("Max value is = {}.".format(max_func(5, 10)))
