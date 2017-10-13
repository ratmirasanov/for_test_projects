"""Task 5."""


import task_4


def translate_func(argument1):
    """Translate string into "robber's language"."""

    new_str = ""
    for letter in argument1:
        if task_4.is_vowel(letter):
            new_str += letter
        else:
            if letter != " ":
                new_str += letter + "o" + letter
            else:
                new_str += " "

    return new_str


print("Translated string into \"robber's language\" is: {}."
      .format(translate_func("I'm speaking Robber's language!")))

# To Do: Нужно обрабатывать еще спецсимволы.
