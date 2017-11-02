"""Task 10."""


import task_9


def overlapping(argument1, argument2):
    """Check that function returns True if they have at least one member in common,
     False otherwise."""

    if isinstance(argument1, list) and isinstance(argument2, list):
        for element1 in argument1:
            for element2 in argument2:
                if task_9.is_member(element1, argument2):
                    return True


print("Is argument1 {} is overlapping with the argument2 {}? {}.".format(
    ["z", "c", "f"], ["a", "v", "x"], overlapping(["z", "c", "f"], ["a", "v", "x"])))
