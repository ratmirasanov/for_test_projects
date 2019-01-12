"""Task 13."""


def max_in_list(argument1):
    """Calculate max value in the list of numbers and return it."""

    if isinstance(argument1, list):

        max_value = argument1[0]

        for index in range(1, len(argument1)):

            if argument1[index] > max_value:

                max_value = argument1[index]

    return max_value


"""
print("The max value in the {} list is: {}."
      .format([5, -4.3, 7, 0], max_in_list([5, -4.3, 7, 0])))
"""
