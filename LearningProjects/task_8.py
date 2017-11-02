"""Task 8."""


import task_7


def is_palindrome(argument1):
    """Recognize palindromes."""

    if str(argument1):
        new_str = argument1.lower()
        print(new_str)
        new_str = ''.join(new_str.split())
        return new_str == task_7.reverse(new_str)
    else:
        return False


print("Is the string palindrome? {}.".format(is_palindrome("Aerate pet area")))
