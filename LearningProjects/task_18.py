"""Task 18."""


def is_pangram(argument1):
    """Check that string is pangram or not."""

    if str(argument1):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            if letter not in argument1.lower():
                return False

        return True


print("String is pangram? {}.".format(is_pangram("The quick brown fox jumps over the lazy dog.")))
