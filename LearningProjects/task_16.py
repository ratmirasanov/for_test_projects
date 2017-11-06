"""Task 14."""


import task_14


def filter_long_words(argument1, number):
    """Takes a list of words and an integer n and returns the list of
     words that are longer than n."""

    if isinstance(argument1, list):
        list_of_lengths = task_14.mapping_words(argument1)
        new_list = []
        for length1, element1 in zip(list_of_lengths, argument1):
            if length1 > number:
                new_list.append(element1)

        return new_list


print("The lengths of the longest words  that are longer than n into \"{}\" list is: {}."
      .format(["test", "Ratmir", "phone"], filter_long_words(["test", "Ratmir", "phone"], 4)))
