"""Task 17."""


import task_8


def is_palindrome_list(argument1):
    """Recognize palindromes in the list."""

    if isinstance(argument1, list):
        new_list = []
        for element1 in argument1:
            if task_8.is_palindrome(element1):
                new_list.append(element1)

        return new_list


print("The palindromes into \"{}\" list are: {}."
      .format(["Go hang a salami I'm a lasagna hog.",
               "Was it a rat I saw?",
               "Step on no pets",
               "Sit on a potato pan, Otis",
               "Lisa Bonet ate no basil",
               "Satan, oscillate my metallic sonatas",
               "I roamed under it as a tired nude Maori",
               "Rise to vote sir",
               "Dammit, I'm mad!",
               "test"],
              is_palindrome_list(["Go hang a salami I'm a lasagna hog.",
                                  "Was it a rat I saw?",
                                  "Step on no pets",
                                  "Sit on a potato pan, Otis",
                                  "Lisa Bonet ate no basil",
                                  "Satan, oscillate my metallic sonatas",
                                  "I roamed under it as a tired nude Maori",
                                  "Rise to vote sir",
                                  "Dammit, I'm mad!",
                                  "test"])))
