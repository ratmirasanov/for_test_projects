"""Task 15."""


import task_13
import task_14


def find_longest_word(argument1):
    """Takes a list of words and returns the length of the longest one."""

    if isinstance(argument1, list):
        return task_13.max_in_list(task_14.mapping_words(argument1))


print("The length of the longest word into \"{}\" list is: {}."
      .format(["test", "Ratmir", "phone"], find_longest_word(["test", "Ratmir", "phone"])))
