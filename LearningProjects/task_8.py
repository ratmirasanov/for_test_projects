"""Task 8."""


import task_7


def is_palindrome(argument1):
    """Recognize palindromes."""

    if str(argument1):
        special_characters = r" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        new_str = ""
        for letter in argument1:
            if letter not in special_characters:
                new_str += letter
        new_str = new_str.lower()
        new_str = ''.join(new_str.split())
        return new_str == task_7.reverse(new_str)


#print("Is the string palindrome? {}.".format(is_palindrome("Aerate pet area")))
