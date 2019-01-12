"""Task 5."""


import task_4


def translate_func(argument1):
    """Translate string into "robber's language"."""

    if str(argument1):

        special_characters = r" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        new_str = ""

        for letter in argument1:

            if task_4.is_vowel(letter) or letter in special_characters:

                new_str += letter

            else:

                new_str += letter + "o" + letter

    return new_str


print("Translated string into \"robber's language\" is: {}."
      .format(translate_func("I'm speaking Robber's language!")))
