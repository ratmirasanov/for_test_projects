"""Task 12."""


def histogram(argument1):
    """Check that function that takes a list of integers and prints a histogram to the screen."""

    if isinstance(argument1, list):

        for element1 in argument1:

            new_str = ""

            for index in range(element1):

                new_str += "*"

            print(new_str + "\n")


print("The histogram of {} is:".format([4, 9, 7]))
histogram([4, 9, 7])
