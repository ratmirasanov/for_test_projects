"""Task 6."""


import task_5


def is_palindrome(argument1):
    """Recognize palindromes."""

    return argument1 == task_5.reverse(argument1)


print("Is the string palindrome? {}".format(is_palindrome("radar")))
