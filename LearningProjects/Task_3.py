"""Task 3."""


def length_of_string(argument1):
    """Calculate length of string and return this value."""

    length_of_str = 0
    for letter in argument1:
        length_of_str += 1

    return length_of_str


print("Length of string is = {}".format(length_of_string("Test string.")))
