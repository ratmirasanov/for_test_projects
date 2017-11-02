"""Task 2."""


import task_1


def max_of_three(argument1, argument2, argument3):
    """Calculate max value of three numbers and return it."""

    if float(repr(argument1)) and float(repr(argument2)) and float(repr(argument3)):
        max_value = task_1.max_func(argument1, argument2)

        return task_1.max_func(argument3, max_value)


print("Max value is = {}.".format(max_of_three(-15, 1, 2.55)))
