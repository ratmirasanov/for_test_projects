"""Task 8."""


import task_7


def is_palindrome(argument1):
    """Recognize palindromes."""

    return argument1 == task_7.reverse(argument1)


print("Is the string palindrome? {}".format(is_palindrome("radar")))
