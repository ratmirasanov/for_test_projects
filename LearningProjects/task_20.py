# -*- coding: utf-8 -*-
"""Task 20."""


BILINGUAL_LEXICON = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "år"
}

def translate(list_of_english_words):
    """Function that takes a list of English words and returns a list of Swedish words."""

    new_list = []
    for element1 in list_of_english_words:
        temp_str = BILINGUAL_LEXICON.get(element1, None)
        if temp_str is not None:
            new_list.append(temp_str)

    return new_list


print("Translated list ({}) of English words to Swedish: {}."
      .format(["happy", "new", "year"], translate(["happy", "new", "year"])))
