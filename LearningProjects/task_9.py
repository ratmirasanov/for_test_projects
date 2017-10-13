"""Task 9."""


def is_member(argument1, argument2):
    """Check that argument1 (value) in the argument2 (list of values)."""

    if isinstance(argument2, list):
        for element in argument2:
            if argument1 == element:
                return True
            else:
                return False


print("Is argument1 {} in the argument2 {}? {}.".format(
    "a", ["a", "b", "x"], is_member("a", ["a", "b", "x"])))
