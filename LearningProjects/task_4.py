"""Task 4."""


def is_vowel(argument1):
    """Check that character is vowel or not."""

    if argument1.isalpha():
        return argument1.lower() in "aeiouy"


print("Character is vowel? {}.".format(is_vowel("A")))
