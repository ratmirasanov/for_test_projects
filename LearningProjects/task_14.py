"""Task 14."""


import task_3


def mapping_words(argument1):
    """Calculate length of an each string into the list of words."""

    if isinstance(argument1, list):
        list_of_lengths = []
        for element1 in argument1:
            list_of_lengths.append(task_3.length_of_string(element1))

        return list_of_lengths


#print("The length of an each string into \"{}\" list is: {}."
#      .format(["test", "Ratmir", "phone"], mapping_words(["test", "Ratmir", "phone"])))
